# Commandes

# Run docker su le port 80

docker run -d --name web-port -p 8080:80 nginx

# Vérification

curl http://localhost:8080

# Afficher les ports

docker ps

# Remove le contener

docker rm web-port

# Run docker sur 127.0.0.1 précisement

docker run -d --name web-port -p 127.0.0.1:8081:80 nginx (port 8080 déjà pris)

# Création Dockerfile

# Build de l'image et lancement du conteneur

docker build -t nginx-expose .
docker run -d --name web-expose nginx-expose

# Afficher les ports

docker ps

# Nettoyage

docker rm -f web-expose
docker rm -f web-port

# Pourquoi un réseau personnalisé est-il recommandé ?

Pour l'isolation et la résolution de noms. Cela permet de regrouper les conteneurs d'un même projet ensemble et d'empêcher des conteneurs extérieurs d'y accéder.

# Quel avantage apporte le DNS interne Docker ?

Il permet aux conteneurs de se parler via leurs noms (ex: serveur) plutôt que par leurs adresses IP. C'est crucial car l'IP d'un conteneur change à chaque redémarrage, mais son nom reste fixe.

# Que permet docker network inspect ?

C'est l'outil de diagnostic ultime. Il permet de voir quels conteneurs sont branchés sur le réseau, leurs adresses IP internes et les options de configuration du sous-réseau.
