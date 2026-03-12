# Commandes

```bash
# Exemple de structure attendue
docker network create app_network
docker volume create db_volume
```
docker network create app_network

docker volume create db_volume

docker run -d  --name mysql_db  --network app_network  -v db_volume:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=root  -e MYSQL_DATABASE=testdb  mysql 

docker run -d --name webapp --network app_network  -p 8080:80  nginx 

docker network inspect app_network

docker exec -it mysql_db mysql -uroot -proot

USE testdb;
CREATE TABLE test (id INT, name VARCHAR(50));
INSERT INTO test VALUES (1,'docker');
SELECT * FROM test;

docker rm -f mysql_db

docker run -d  --name mysql_db  --network app_network  -v db_volume:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=root  -e MYSQL_DATABASE=testdb  mysql

docker exec -it mysql_db mysql -uroot -p

root

docker rm -f webapp mysql_db

docker network rm app_network

docker volume rm db_volume
