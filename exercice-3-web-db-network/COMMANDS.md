docker network create app_network
docker volume create db_volume  
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb mysql
docker network inspect app_network
docker exec -it mysql_db mysql -uroot -proot testdb
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));
INSERT INTO users (name) VALUES ('florian');
SELECT * FROM users;
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb mysql
docker exec -it mysql_db mysql -uroot -proot testdb
SELECT * FROM users;


1)
il n'y a besoin d'accéder à la base de donnée depuis la machine hote et elle est relie au network

2)
Le réseau personnalisé permet d'avoir un DNS interne Docker et une communication par nom de conteneur

3)
MySQL démarre avec un stockage vide et toutes les données sont perdues