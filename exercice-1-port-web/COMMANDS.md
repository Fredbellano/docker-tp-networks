# Commandes

```bash
# Exemple de structure attendue
docker run -d --name web-port -p 8080:80 nginx
```

```bash
docker port web-port
```

```bash
docker rm web-port
```

```bash
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
```

```bash
docker stop web-port
docker rm web-port
```
