# Commandes

# Création du réseau et du volume
docker network create app_network
docker volume create db_volume

# Lancement de MySQL sur le réseau personnalisé avec volume
docker run -d \
  --name mysql_db \
  --network app_network \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=testdb \
  -v db_volume:/var/lib/mysql \
  mysql:8

# Lancement du conteneur web sur le même réseau, exposé vers l'hôte
docker run -d \
  --name webapp \
  --network app_network \
  -p 8080:80 \
  nginx

# Vérification du service web
curl http://localhost:8080

# Inspection du réseau
docker network inspect app_network

# Insertion d'une donnée dans MySQL
docker exec -i mysql_db mysql -uroot -prootpass testdb -e "CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, content VARCHAR(255)); INSERT INTO messages (content) VALUES ('Bonjour Docker');"

# Vérification de la donnée
docker exec -i mysql_db mysql -uroot -prootpass testdb -e "SELECT * FROM messages;"

# Suppression du conteneur MySQL uniquement
docker rm -f mysql_db

# Recréation du conteneur MySQL avec le même volume
docker run -d \
  --name mysql_db \
  --network app_network \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=testdb \
  -v db_volume:/var/lib/mysql \
  mysql:8

# Vérification que la donnée est toujours présente
docker exec -i mysql_db mysql -uroot -prootpass testdb -e "SELECT * FROM messages;"

# Nettoyage final
docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume

# Pourquoi la base de données n’a-t-elle pas besoin d’être exposée vers l’hôte dans cette architecture ?

La base de données est utilisée uniquement par les autres conteneurs de l’application, en particulier webapp.
Comme mysql_db est déjà accessible depuis le réseau Docker app_network, il n’est pas nécessaire d’ouvrir son port vers la machine hôte.
Cela améliore aussi la sécurité en évitant d’exposer inutilement la base de données à l’extérieur.



# En quoi le réseau personnalisé simplifie-t-il la communication entre services ?

Le réseau personnalisé permet aux conteneurs de communiquer directement entre eux par leur nom, par exemple mysql_db.
Docker fournit un DNS interne qui évite d’avoir à chercher ou configurer manuellement les adresses IP.
Cela rend l’architecture plus simple, plus propre et plus facile à maintenir.


#   Que se passerait-il si le volume n’était pas réutilisé après recréation du conteneur MySQL ?

Si le volume n’était pas réutilisé, les données stockées dans MySQL seraient perdues après la suppression du conteneur.
Le nouveau conteneur repartirait avec une base vide, comme une nouvelle installation.
Le volume est donc indispensable pour conserver les données entre deux recréations du conteneur.
