
# Commandes

```bash
docker run -d --name web-port -p 8080:80 nginx
docker ps
docker port web-port
docker rm -f web-port
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
curl -sI http://localhost:8080 | head -n 5
docker rm -f web-port || true
```