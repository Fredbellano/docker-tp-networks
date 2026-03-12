# Commandes

```bash
# Exemple de structure attendue
1. docker run -d --name web-port -p 8080:80 nginx
```
4. 
# afficher les ports publiés du conteneur
docker port web-port


5. 
# supprimer le conteneur précedent
docker rm -f web-port

# Relancer le service avec une écoute restreinte sur 127.0.0.1
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx


6. 
# Construire l'image
docker build -t nginx-expose .

# Lancer le conteneur
docker run -d --name web-expose nginx-expose

7.
# Nettoyer les conteneurs
docker rm -f web-port web-expose

