# 1 
```bash
docker network create test_net
```

# 2 
```bash
docker run -d --name serveur --network test_net nginx
```

# 3
```bash
docker run --rm --network test_net alpine ping -c 3 serveur
```

# 4
```bash
docker network inspect test_net
```

# 5 
```bash
docker run -d --name web-default nginx
```

# 6 
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-default
```

# 7 
```bash
docker run --rm alpine ping -c 3 172.21.0.2
```

# 8 
```bash
docker network connect test_net web-default
```

# 9 
```bash
docker network inspect test_net
```

# 10 
```bash
docker network disconnect test_net web-default
```

# 11
```bash
docker rm -f serveur web-default
docker network rm test_net
```