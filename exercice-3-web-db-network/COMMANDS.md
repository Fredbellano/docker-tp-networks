# Commandes

```bash
# Exemple de structure attendue
docker network create app_network
docker volume create db_volume
```

```bash
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql mysql:8
```

```bash
docker run -d --name webapp --network app_network -p 8080:80 nginx
```

```bash
docker network inspect app_network
```

```bash
docker exec -it mysql_db mysql

USE testdb;

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50)
);

INSERT INTO users (name) VALUES ('Bob');

SELECT * FROM users;
```

```bash
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql mysql:8
```

```bash
docker exec -it mysql_db mysql

USE testdb;
SELECT * FROM users;
```

```bash
docker rm -f mysql_db webapp
docker network rm app_network
docker volume rm db_volume
```