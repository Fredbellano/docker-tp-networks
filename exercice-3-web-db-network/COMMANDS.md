# COMMANDS.md

# Créer le réseau
docker network create app_network


# Créer le volume
docker volume create db_volume


# Lancer le conteneur MySQL
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -v db_volume:/var/lib/mysql mysql:8


# Lancer le conteneur webapp
docker run -d --name webapp --network app_network -p 8080:80 nginx


# Vérifier les conteneurs dans le réseau
docker network inspect app_network


# Insérer une donnée

docker exec -it mysql_db mysql -u root -p
puis

USE testdb;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50)
);

INSERT INTO users (name) VALUES ('Alexandre');

SELECT * FROM users;


# Supprimer puis recréer le conteneur MySQL
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -v db_volume:/var/lib/mysql mysql:8


# Vérifier que la donnée est toujours présente
docker exec -it mysql_db mysql -u root -p
USE testdb;
SELECT * FROM users;


# Nettoyer les conteneurs, le réseau et le volume

docker rm -f mysql_db webapp
docker network rm app_network
docker volume rm db_volume



1. Pourquoi la base de données n’a pas besoin d’être exposée vers l’hôte ?
Parce que seule l’application web doit y accéder. Les deux conteneurs sont dans le même réseau Docker. Ils peuvent donc communiquer directement entre eux.

2. En quoi le réseau personnalisé simplifie la communication ?
Les conteneurs peuvent se trouver avec leur nom. Par exemple webapp peut se connecter à mysql_db, il n’est pas nécessaire d'avoir l’adresse IP grâce au DNS interne docker.

3. Que se passerait-il si le volume n’était pas réutilisé ?
Les données seraient perdues. Le nouveau conteneur MySQL démarrerait avec une base vide. Le volume sert à conserver les données.