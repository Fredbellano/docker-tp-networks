# Commandes

```bash
# Exemple de structure attendue
docker network create app_network

docker volume create db_volume

docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:8.0

docker run -d --name webapp --network app_network -p 8080:80 Nginx

docker network inspect app_network

docker exec -it mysql_db mysql -proot -e "CREATE DATABASE tp_docker;"

docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:8.0

docker exec -it mysql_db mysql -proot -e "SHOW DATABASES;"

docker rm -f webapp mysql_db

docker network rm app_network

docker volume rm db_volume

Q1 : 
Pour la séurité, seule l'application web a besoin de lui parler, on empêche toute attaque extérieur directe sur la base de donnée et cachant les ports

Q2 : 
Grâce au DNS interne, la webapp peut contacter la base et utilisant le nom d'hôte 

Q3 : 
toutes les données seraient perdu. MySQL recréer une BDD vide au démarrage du nouveau containeur
```
