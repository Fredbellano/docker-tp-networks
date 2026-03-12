# 1
```bash
docker network create app_network
```

# 2
```bash
docker volume create db_volume
```

# 3
```bash
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=appdb mysql:8
```

# 4
```bash
docker run -d --name webapp --network app_network -p 8080:80 nginx
```

# 5
http://localhost:8080

# 6
```bash
docker network inspect app_network
```

# 7
```bash
docker exec mysql_db mysql -uroot -prootpass -e "SELECT 1;"
```

# 8
```bash
docker exec mysql_db mysql -uroot -prootpass appdb -e "CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255)); INSERT INTO notes (message) VALUES ('donnee persistante');"
```

# 9
```bash
docker exec mysql_db mysql -uroot -prootpass appdb -e "SELECT * FROM notes;"
```

# 10
```bash
docker rm -f mysql_db
```

# 11
```bash
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=appdb mysql:8
```

# 12
```bash
docker exec mysql_db mysql -uroot -prootpass -e "SELECT 1;"
```

# 13
```bash
docker exec mysql_db mysql -uroot -prootpass appdb -e "SELECT * FROM notes;"
```

# 14
```bash
docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume
```