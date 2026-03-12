# Commandes

```bash
# Exemple de structure attendue
docker network create app_network
docker volume create db_volume
```
3.
# lancer conteneur mysql connecté à app_network et utilisant db_volume

docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -v db_volume:/var/lib/mysql mysql:8.0

4.
# Lancer le conteneur webapp connecté au meme reseau et publier sur http://localhost:8080
docker run -d --name webapp --network app_network -p 8080:80 nginx

5.
# Verifier que webapp et mysql_db apparaissent
docker network inspect app_network

6.
# Créer la base
docker exec -it mysql_db mysql -uroot -proot -e "CREATE DATABASE testdb;"

# Inserer une donnée dans la base
docker exec -it mysql_db mysql -uroot -proot -D testdb -e "CREATE TABLE utilisateurs (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50)); INSERT INTO utilisateurs (nom) VALUES ('Corentin');"

# verifier la présence
docker exec -it mysql_db mysql -uroot -proot -D testdb -e "SELECT * FROM utilisateurs;"


7.
# supprimer puis recrer le conteneur mysql_db avec le meme volume
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -v db_volume:/var/lib/mysql mysql:8

8.
# verifier que la donnée est toujours présente
docker exec -it mysql_db mysql -uroot -proot -D testdb -e "SELECT * FROM utilisateurs;"

9.
# Nettoyer les conteneurs, le réseau et volume
docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume