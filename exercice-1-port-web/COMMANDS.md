# 1 
```bash
docker run -d --name web-port -p 8080:80 nginx
```

# 2 
http://localhost:8080

# 3 
```bash
docker port web-port
```

# 4 
```bash
docker rm -f web-port
```

# 5 
```bash
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
```

# 6 
```bash
http://127.0.0.1:8080
```

# 7 
```bash
docker port web-port
```

# 8 
```bash
docker image inspect nginx --format '{{json .Config.ExposedPorts}}'
```

# 9
```bash
docker rm -f web-port
```