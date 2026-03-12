# Commandes
# Création du réseau personnalisé
docker network create test_net

# Lancer un conteneur nginx sur le réseau personnalisé
docker run -d --name serveur --network test_net nginx

# Depuis un conteneur alpine éphémère, tester la résolution DNS et l'accès au serveur
docker run --rm --network test_net alpine sh -c "apk add --no-cache curl bind-tools >/dev/null && nslookup serveur && curl http://serveur"

# Inspecter le réseau personnalisé
docker network inspect test_net

# Test sur le réseau bridge par défaut
docker run -d --name serveur-bridge nginx
docker run --rm alpine sh -c "apk add --no-cache curl bind-tools >/dev/null && nslookup serveur-bridge || true && curl http://serveur-bridge || true"

# Connecter à chaud un conteneur existant au réseau personnalisé
docker network connect test_net serveur-bridge

# Vérifier qu'il est joignable sur le réseau personnalisé
docker run --rm --network test_net alpine sh -c "apk add --no-cache curl bind-tools >/dev/null && nslookup serveur-bridge && curl http://serveur-bridge"

# Déconnecter le conteneur du réseau personnalisé
docker network disconnect test_net serveur-bridge

# Nettoyage des conteneurs
docker rm -f serveur serveur-bridge

# Suppression du réseau
docker network rm test_net
# Pourquoi l’utilisation d’un réseau personnalisé est-elle recommandée pour des applications multi-conteneurs ?

Un réseau personnalisé permet une communication plus simple et plus propre entre les conteneurs.
Les conteneurs connectés à ce réseau peuvent se joindre directement par leur nom et sont isolés des autres conteneurs qui ne sont pas sur ce réseau

# Quel avantage apporte le DNS interne Docker ?

Le DNS interne Docker permet de résoudre automatiquement le nom d’un conteneur en adresse IP.
Cela signifie que les conteneurs peuvent communiquer entre eux en utilisant simplement leur nom, sans avoir besoin de connaître leur adresse IP.



# Que permet docker network inspect dans une phase de diagnostic ?

La commande docker network inspect permet d’afficher les informations détaillées d’un réseau Docker, comme les conteneurs connectés, leurs adresses IP et les paramètres du réseau.
Elle est utile pour diagnostiquer les problèmes de communication entre conteneurs.


