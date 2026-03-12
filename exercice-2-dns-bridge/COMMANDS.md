# Commandes

```bash
# Exemple de structure attendue
docker network create test_net

# Lancer le conteneur serveur sur ce réseau
docker run -d --name serveur --network test-net nginx

# Tester la résolution DNS depuis un conteneur Alpine
docker run --rm --network test-net alpine ping -c 2 serveur

# Inspecter le réseau
docker network inspect test-net

# Test rapide sur le réseau bridge par défaut
docker run --rm --network bridge alpine ping -c 2 serveur

# Connecter un conteneur existant à chaud
docker run -d --name temp-nginx nginx
docker network connect test-net temp-nginx
docker run --rm --network test-net alpine ping -c 2 temp-nginx

# Déconnecter le conteneur et supprimer le réseau
docker network disconnect test-net temp-nginx
docker rm -f serveur temp-nginx
docker network rm test-net
