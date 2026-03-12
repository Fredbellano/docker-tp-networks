# Commandes

```bash
# créer le réseau
docker network create test_net

# lancer nginx sur ce réseau
docker run -d --name serveur --network test_net nginx

# tester si on peut joindre "serveur" depuis un autre conteneur
docker run --rm --network test_net alpine ping -c 3 serveur

# regarder les infos du réseau
docker network inspect test_net

# test sur le réseau bridge par défaut
docker run -d --name serveur-bridge nginx
docker run --rm alpine ping -c 3 serveur-bridge

# connecter un conteneur existant au réseau
docker run -d --name web-port nginx
docker network connect test_net web-port

# vérifier les conteneurs dans le réseau
docker network inspect test_net

# déconnecter le conteneur
docker network disconnect test_net web-port

# nettoyage
docker stop serveur serveur-bridge web-port
docker rm serveur serveur-bridge web-port
docker network rm test_net