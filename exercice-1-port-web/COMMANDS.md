docker run -d --name web-port -p 8080:80 nginx
docker ps
docker stop web-port
docker rm web-port
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
docker stop web-port
docker rm web-port

1)
Port conteneur : port utilisé par l'application à l'intérieur du conteneur
Port hôte : port de la machine physique utilisé pour accéder au conteneur depuis l'extérieur

2)
documenter le port utilisé
informer Docker que l'application écoute sur ce port
il ne publie pas le port vers l'hôte.

3)
Pour faire des test en local