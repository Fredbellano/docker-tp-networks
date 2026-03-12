# Commandes

```bash
docker network create app_network
docker volume create db_volume
docker run -d --name mysql_db --network app_network -v db_volume -e MYSQL_ROOT_PASSWORD=rootpassword mysql
docker run -d --name webapp --network app_network -p 8080:80 nginx  
docker network inspect app_network #les deux apparaissent bien
docker exec -it mysql_db mysql -uroot -prootpassword
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));
INSERT INTO users (name) VALUES ('Alice');
SELECT * FROM users;
exit
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -v db_volume -e MYSQL_ROOT_PASSWORD=rootpassword mysql
docker exec -it mysql_db mysql -uroot -prootpassword
SELECT * FROM users;
exit
docker rm -f mysql_db & docker rm -f webapp & docker network rm app_network & docker volume rm db_volume  
```

Questions de reflexion
Pourquoi la base de donnees n'a-t-elle pas besoin d'etre exposee vers l'hote dans cette architecture ?
En quoi le reseau personnalise simplifie-t-il la communication entre services ?
Que se passerait-il si le volume n'etait pas reutilise apres recreation du conteneur MySQL ?

- Parce que les conteneurs se trouvent sur le même réseau docker donc ils peuvent intéragir ensemble avec le DNS
- Avec le DNS qui permet d'appeler les services facilement
- Le conteneur sql démarrerais sans les données précédentes