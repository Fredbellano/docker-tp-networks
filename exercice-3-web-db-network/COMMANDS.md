# Commandes

```bash
# créer le réseau
docker network create app_network

# créer le volume
docker volume create db_volume

# lancer mysql avec le volume
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -v db_volume:/var/lib/mysql mysql:8

# lancer le conteneur web
# j'utilise 8083 car 8080 était déjà pris sur ma machine
docker run -d --name webapp --network app_network -p 8083:80 nginx

# vérifier les conteneurs dans le réseau
docker network inspect app_network

# créer une table, ajouter une donnée et vérifier
docker exec -it mysql_db mysql -uroot -proot -D testdb -e "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50)); INSERT INTO users (nom) VALUES ('test'); SELECT * FROM users;"

# supprimer puis recréer mysql avec le même volume
docker stop mysql_db
docker rm mysql_db
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -v db_volume:/var/lib/mysql mysql:8

# vérifier que la donnée est toujours là
docker exec -it mysql_db mysql -uroot -proot -D testdb -e "SELECT * FROM users;"

# nettoyage
docker stop webapp mysql_db
docker rm webapp mysql_db
docker network rm app_network
docker volume rm db_volume