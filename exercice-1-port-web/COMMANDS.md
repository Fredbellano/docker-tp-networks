# Commandes

```bash
# Exemple de structure attendue
docker run -d --name web-port -p 8080:80 nginx

docker ps

docker rm web-port

docker run -d --name web-port -p 127.0.0.1:8080:80 nginx

Le port hote 8080 c'est le port de la machine qui permet d'acceder au service, alors que le port conteneur 80 est utilisé à l'intérieur du conteneur par l'application.

L'instruction `EXPOSE` n'ouvre pas vraiment le port mais juste montre les ports utilisés tandis que `-p` les rend accessible.

Limiter l'ecoute a `127.0.0.1` est-il utile pour les services internes et le developpement local le cas par exemple des API ou base de données.

docker rm web-port
```
