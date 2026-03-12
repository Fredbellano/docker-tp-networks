# Commandes
# Lancer le conteneur nginx et publier le port
docker run -d --name web-port -p 8080:80 nginx

# Vérifier que le service répond
curl http://localhost:8080

# Afficher les ports publiés
docker port web-port

# Supprimer le conteneur
docker rm -f web-port

# Relancer nginx avec une publication limitée à localhost
docker run -d --name web-port-local -p 127.0.0.1:8080:80 nginx

# Vérifier que le service répond
curl http://localhost:8080

# Voir les ports publiés
docker port web-port-local

# Nettoyer
docker rm -f web-port-local

# Quelle est la différence entre le port hôte et le port conteneur ?
Le port hôte est le port ouvert sur la machine physique. Le port conteneur est le port utilisé par l’application à l’intérieur du conteneur.

# Pourquoi EXPOSE ne suffit-il pas ?
EXPOSE documente le port utilisé par l’image, mais n’ouvre pas le port vers l’extérieur. Pour rendre le service accessible depuis la machine hôte, il faut publier le port avec -p.

# Dans quel cas limiter l’écoute à 127.0.0.1 est-il utile ?
C’est utile quand on veut que le service soit accessible uniquement depuis la machine locale, par exemple pour du dev, des tests, ou pour éviter une exposition réseau inutile.
