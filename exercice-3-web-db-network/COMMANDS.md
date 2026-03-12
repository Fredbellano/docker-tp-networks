docker network create app_network
docker volume create db_volume
docker run -d --name mysql_db --network app_network \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=tpdb \
  -v db_volume:/var/lib/mysql \
  mysql:8
docker run -d --name webapp --network app_network -p 8080:80 nginx
curl http://localhost:8080
docker network inspect app_network
docker exec mysql_db sh -c 'until mysqladmin ping -h localhost -uroot -p"$MYSQL_ROOT_PASSWORD" --silent; do sleep 1; done'
docker exec mysql_db mysql -uroot -prootpass -e "USE tpdb; CREATE TABLE notes (id INT AUTO_INCREMENT PRIMARY KEY, contenu VARCHAR(255)); INSERT INTO notes (contenu) VALUES ('donnee_persistante');"
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=tpdb \
  -v db_volume:/var/lib/mysql \
  mysql:8
docker exec mysql_db sh -c 'until mysqladmin ping -h localhost -uroot -p"$MYSQL_ROOT_PASSWORD" --silent; do sleep 1; done'
docker exec mysql_db mysql -uroot -prootpass -e "USE tpdb; SELECT * FROM notes;"
docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume

- La DB a pas besoin d'etre exposee: seule la webapp doit parler avec, donc on la garde en interne pour la securite.
- Le reseau perso simplifie tout: les services se parlent par nom (`mysql_db`, `webapp`) sans config chelou.
- Si tu recrees MySQL sans reutiliser le volume, tu repars a zero et tu perds les donnees.
