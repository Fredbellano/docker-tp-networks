# COMMANDS.md

# 1. Créer le réseau personnalisé

docker network create app_network

# 2. Créer le volume de persistance

docker volume create db_volume

# 3. Lancer MySQL connecté au réseau avec le volume

docker run -d \
 --name mysql_db \
 --network app_network \
 -e MYSQL_ROOT_PASSWORD=rootpass \
 -e MYSQL_DATABASE=appdb \
 -v db_volume:/var/lib/mysql \
 mysql:8.0

# Vérifier que MySQL est bien démarré

docker ps

# 4. Lancer le conteneur web exposé sur localhost:8080

docker run -d \
 --name webapp \
 --network app_network \
 -p 8080:80 \
 nginx:alpine

# Vérifier l’accès au service web

curl http://localhost:8080

# 5. Vérifier les conteneurs dans l’inspection du réseau

docker network inspect app_network

# 6. Insérer une donnée dans MySQL

docker exec -it mysql_db mysql -uroot -prootpass -e "
USE appdb;
CREATE TABLE IF NOT EXISTS messages (
id INT AUTO_INCREMENT PRIMARY KEY,
contenu VARCHAR(255) NOT NULL
);
INSERT INTO messages (contenu) VALUES ('Bonjour Docker');
SELECT \* FROM messages;
"

# 7. Supprimer puis recréer uniquement le conteneur mysql_db avec le même volume

docker rm -f mysql_db

docker run -d \
 --name mysql_db \
 --network app_network \
 -e MYSQL_ROOT_PASSWORD=rootpass \
 -e MYSQL_DATABASE=appdb \
 -v db_volume:/var/lib/mysql \
 mysql:8.0

# Attendre quelques secondes puis vérifier que MySQL est prêt

docker ps

# 8. Vérifier que la donnée est toujours présente

docker exec -it mysql_db mysql -uroot -prootpass -e "
USE appdb;
SELECT \* FROM messages;
"

# 9. Nettoyage final

docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume
