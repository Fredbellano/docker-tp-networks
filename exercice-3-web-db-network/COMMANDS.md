# Commandes

```bash
# Exemple de structure attendue
docker network create app_network
docker volume create db_volume

docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=testdb mysql:8

docker network inspect app_network

docker exec -it mysql_db mysql -uroot -prootpass

docker stop mysql_db
docker rm mysql_db

docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass mysql:8

docker exec -it mysql_db mysql -uroot -prootpass

docker stop webapp mysql_db
docker rm webapp mysql_db
docker network rm app_network
docker volume rm db_volume

La base de donnée n'a pas besoin car elle est accessible depuisvle reseau docker.

L'utilisation d'un reseau personnalise est recommandee pour des applications multi-conteneurs car ça permet une isolation réseau, une résolution rapide du DNS via le nom et une communication simple entre coneneur.

Si le volume n'etait pas reutilisé les données serait stocker dans le conteneur.

```
