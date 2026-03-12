# Commandes


## 1. Lancer un conteneur `nginx` nomme `web-port`.
## 2. Publier le port `80` du conteneur sur le port `8080` de la machine hote.

```bash
docker run -d --name web-port -p 8080:80 nginx
```

## 3. Verifier que le service repond sur `http://localhost:8080`.

```bash
curl http://localhost:8080
```
## 4. Afficher les ports publies du conteneur.

```bash
docker port web-port
```
## 5. Relancer le meme service avec une publication restreinte a `127.0.0.1`.

```bash
docker rm web-port
```
```bash
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
```
```bash
curl http://127.0.0.1:8080
```
## 6. Comparer ce que vous observez avec une simple declaration `EXPOSE` dans une image.

### On teste avec un dockerfile

```Dockerfile
FROM nginx
EXPOSE 80
```
### Construire l'image :

```bash
docker build -t nginx-expose .
```

### Lancer le conteneur  sans préciser le -p

```bash
docker run -d --name web-expose nginx-expose
```

### --> le local host ne répondra pas pour ce conteneur

##  6. Nettoyage final

```bash
docker rm -f web-port web-expose
```

## Questions de reflexion

- Quelle est la difference entre le port hote et le port conteneur ?

    le port hote est celui ouvert sur la machine

- Pourquoi `EXPOSE` ne suffit-il pas a rendre le service accessible ?

    Expose est simplement la pour de la documentation et ne publie rien 

- Dans quel cas limiter l'ecoute a `127.0.0.1` est-il utile ?

    Il sert si on veut limiter l'utilisation à la machine locale