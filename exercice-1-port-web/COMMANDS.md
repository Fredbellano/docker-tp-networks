# Commandes

```bash
# Questions 1, 2 et 3
docker run -d --name web-port -p 8080:80 nginx
```

# afficher les ports publiés du conteneur
docker port web-port

# Relancer le meme service
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx

# L'EXPOSE ne publie pas les ports, c'est simplement pour de la documentation



# Questions
- Quelle est la difference entre le port hote et le port conteneur ?
Le port hôte est le port de sortie de notre machine vers le conteneur, et le port conteneur est la porte d'entrée vers celui-ci. En liant les deux, on relie les deux portes. Par exemple, le port 8080 permet de sortir de notre machine et d'entrer dans le conteneur via son port 80.

- Pourquoi `EXPOSE` ne suffit-il pas a rendre le service accessible ?
Car EXPOSE n'est que du déclaratif, il sert dans l'image pour préciser qu'un port est accessible et possible d'ouvrir. Alors que -p permet de faire la liaison active entre deux ports lors du démarrage du conteneur.

- Dans quel cas limiter l'ecoute a `127.0.0.1` est-il utile ?
Limiter l'écoute à 127.0.0.1 (ou "localhost") permet de restreindre l'accès au conteneur à l'hôte uniquement.