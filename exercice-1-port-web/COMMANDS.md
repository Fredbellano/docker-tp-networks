# Commandes

```bash
# 1) Lancer nginx et publier 80 (conteneur) vers 8080 (hote)
docker run -d --name web-port -p 8080:80 nginx

# 2) Verifier l'accessibilite depuis la machine hote
curl http://localhost:8080

# 3) Afficher les ports publies
docker port web-port
docker inspect web-port --format '{{json .NetworkSettings.Ports}}'

# 4) Relancer le meme service avec une publication restreinte a 127.0.0.1
docker rm -f web-port
docker run -d --name web-port-local -p 127.0.0.1:8080:80 nginx
curl http://127.0.0.1:8080
docker port web-port-local

# 5) Comparer avec EXPOSE (metadonnee image, sans publication hote)
docker image inspect nginx --format '{{json .Config.ExposedPorts}}'
docker run -d --name web-no-publish nginx
docker ps --filter name=web-no-publish

# 6) Nettoyage
docker rm -f web-port-local web-no-publish
```

## Reponses aux questions de reflexion

1. Difference entre port hote et port conteneur:
Le port conteneur est le port sur lequel l'application ecoute dans le conteneur (ex: 80). Le port hote est le port de la machine locale expose vers l'exterieur (ex: 8080). Le mapping se fait avec -p hote:conteneur.

2. Pourquoi EXPOSE ne suffit pas:
EXPOSE est une metadonnee d'image qui documente les ports attendus. Cela ne publie pas le port sur la machine. Pour rendre le service accessible depuis l'hote, il faut utiliser -p ou -P au lancement du conteneur.

3. Utilite de limiter a 127.0.0.1:
Cela restreint l'acces au service a la machine locale uniquement. C'est utile pour le developpement, les tests locaux, et pour eviter une exposition reseau inutile.
