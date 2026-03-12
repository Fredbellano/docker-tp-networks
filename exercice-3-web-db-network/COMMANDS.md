# Commandes

```bash
docker network create app_network

docker volume create db_volume

docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=testdb mysql:8.0

docker run -d --name webapp --network app_network -p 8080:80 nginx:latest

docker network inspect app_network

docker exec -i mysql_db mysql -uroot -proot123 testdb -e "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)); INSERT INTO users (name) VALUES ('Alice Dupont'), ('Bob Martin');"

docker exec -i mysql_db mysql -uroot -proot123 testdb -e "SELECT * FROM users;"

docker stop mysql_db

docker rm mysql_db

docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=testdb mysql:8.0

docker exec -i mysql_db mysql -uroot -proot123 testdb -e "SELECT * FROM users;"

docker stop webapp mysql_db

docker rm webapp mysql_db

docker network rm app_network

docker volume rm db_volume
```
