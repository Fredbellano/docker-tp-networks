from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'mysql_db')
DB_USER = os.environ.get('DB_USER', 'demo_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'demo_pass')
DB_NAME = os.environ.get('DB_NAME', 'demo_db')

def get_conn():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )

@app.route('/')
def index():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM info')
        cnt = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f'webapp OK — rows={cnt}\n'
    except Exception as e:
        return f'ERROR: {e}\n', 500

@app.route('/init')
def init_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS info (id INT AUTO_INCREMENT PRIMARY KEY, txt VARCHAR(100))')
    cur.execute("INSERT INTO info (txt) VALUES ('hello')")
    cur.close()
    conn.close()
    return 'initialized\n'

@app.route('/show')
def show():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, txt FROM info')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return '\n'.join(f'{r[0]}:{r[1]}' for r in rows) + '\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
