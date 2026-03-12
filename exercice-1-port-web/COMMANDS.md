# Commandes

```bash
- docker run -d --name web-port -p 8080:80 nginx   
- curl http://localhost:8080/
```

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html> 
``` 

```bash
- docker port web-port
```
```
- 80/tcp -> 0.0.0.0:8080
- 80/tcp -> [::]:8080
```

```bash
- docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
```
```bash
- docker port web-port
```
```
- 80/tcp -> 127.0.0.1:8080
````

- L'EXPOSE dans l'image sert juste à documenter donc on pourrait très bien ne pas mettre se port, on peut dire que c'est le port recommander par défaut
```bash
- docker rm -f web-port
```

- Questions de reflexion

    - Quelle est la difference entre le port hote et le port conteneur ?
      - Le port hote permet d'accéder au conteneur, le port du conteneur est le port dédié à l'application dans celui-ci
    - Pourquoi EXPOSE ne suffit-il pas a rendre le service accessible ?
      - C'est de la documentation dans le fichier image
    - Dans quel cas limiter l'ecoute a 127.0.0.1 est-il utile ?
      - Sécurité et des tests, cela veut dire qu'il est accessible uniquement depuis la machine hôte du réseau
