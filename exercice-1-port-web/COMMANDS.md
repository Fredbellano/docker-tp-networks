# Commandes

``` bash
# Exemple de structure attendue
docker run -d --name web-port -p 8080:80 nginx

# Vérification accessibilité
curl.exe -I http://localhost:8080

#Vérifier les ports
docker port web-port

#Suppression du conteneur
docker rm -f web-port

#Nouveau conteneur avec publication restreinte
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx

#Nettoyage final
docker rm -f web-port

``` 

Une simple commande EXPOSE ne publie pas vers la machine hôte

# Réponse aux questions

1) Le port hote est le point d'entrée sur la machine physique tandis que le port conteneur est le point d'écoute interne défini par l'app au sein du network namespace

2) L'instruction EXPOSE n'ouvre aucun port, elle ne sert qu'à documenter 

3) Limiter au port 127.0.0.1 permet d'empêcher l'accès au service depuis toute machine n'étant pas la machine hôte 


