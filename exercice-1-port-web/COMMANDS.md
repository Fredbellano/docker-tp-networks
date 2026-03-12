# Commandes

```bash
# lancer nginx dans un conteneur
# j'utilise 8082 sur ma machine car 8080 est déjà utilisé
docker run -d --name web-port -p 8082:80 nginx

# vérifier que le conteneur tourne
docker ps

# voir quel port est publié
docker port web-port

# arrêter et supprimer le conteneur pour refaire le test
docker stop web-port
docker rm web-port

# relancer nginx mais accessible seulement en local
docker run -d --name web-port -p 127.0.0.1:8082:80 nginx

# vérifier à nouveau
docker ps
docker port web-port

# nettoyage
docker stop web-port
docker rm web-port