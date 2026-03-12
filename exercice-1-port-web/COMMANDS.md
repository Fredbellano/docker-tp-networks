# Commandes

```bash
# Exemple de structure attendue
docker run -d --name web-port -p 8080:80 Nginx

docker port web-port

docker rm -f web-port

docker run -d --name web-port -p 127.0.0.1:8080:80 Nginx

docker rm -f web-port

Q1 : 
Le port conteneur est le port interne sur lequel l'application écoute. Le port hôte est celui exposé sur notre machine physique pour permettre l'accès au conteneur depuis l'extérieur

Q2 : 
'EXPOSE' est une instruction informative qui documente quel port l'image a l'intention d'utiliser. Seule l'option -p au moment du docker run créer réellement les règles de routage sur la machine hôte

Q3 : 
C'est une pratique de sécurité necéssaire pour s'assurer que le service n'est pas exposé sur un réseau public ou local
```
