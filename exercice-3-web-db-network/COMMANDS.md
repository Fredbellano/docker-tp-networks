# Commandes

```bash
# 1) Creer le reseau et le volume
docker network create app_network
docker volume create db_volume

# 2) Lancer MySQL dans le reseau (non expose vers l'hote)
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=appdb -v db_volume:/var/lib/mysql mysql:8

# 3) Lancer l'application web sur le meme reseau, exposee en 8080
docker run -d --name webapp --network app_network -p 8080:80 nginx
curl http://localhost:8080

# 4) Verifier que les 2 conteneurs sont dans app_network
docker network inspect app_network

# 5) Inserer une donnee et verifier sa presence
docker exec -i mysql_db mysql -uroot -prootpass appdb -e "CREATE TABLE IF NOT EXISTS notes(id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255));"
docker exec -i mysql_db mysql -uroot -prootpass appdb -e "INSERT INTO notes(message) VALUES('hello from docker network');"
docker exec -i mysql_db mysql -uroot -prootpass appdb -e "SELECT * FROM notes;"

# 6) Supprimer puis recreer uniquement mysql_db avec le meme volume
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=appdb -v db_volume:/var/lib/mysql mysql:8

# 7) Re-verifier la persistence des donnees
docker exec -i mysql_db mysql -uroot -prootpass appdb -e "SELECT * FROM notes;"

# 8) Nettoyage final
docker rm -f webapp mysql_db
docker network rm app_network
docker volume rm db_volume
```

## Reponses aux questions de reflexion

1. Pourquoi la base n'a pas besoin d'etre exposee vers l'hote:
Dans cette architecture, seule l'application web doit etre accessible depuis l'exterieur. La base doit rester interne pour reduire la surface d'attaque et limiter les acces directs non necessaires.

2. En quoi le reseau personnalise simplifie la communication:
Les services partagent le meme reseau et peuvent se contacter par nom de conteneur (ex: mysql_db), ce qui evite de configurer des IP fixes et facilite les deploiements.

3. Sans reutilisation du volume apres recreation MySQL:
Les donnees seraient perdues (ou la base repartirait vide) car elles resteraient dans l'ancien systeme de fichiers conteneur, qui disparait lors de la suppression du conteneur.
