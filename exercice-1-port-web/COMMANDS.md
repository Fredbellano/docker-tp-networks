# Commandes

```bash
# Exemple de structure attendue
docker run -d --name web-port -p 8080:80 nginx

docker ps

docker port web-port

docker rm -f web-port

docker run -d --name web-port -p 127.0.0.1:8080:80 nginx

docker rm -f web-port