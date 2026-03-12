# Commandes

# Créer un réseau docker personnalisé
docker network create test_net

# Lancer le conteneur nginx nommé serveur
docker run -d --name serveur --network test_net nginx

# Conteneur ephemere, ping serveur pour vérifier qu'il est joignable
docker run --rm --network test_net alpine ping -c 3 serveur

# Inspecter le réseau
docker network inspect test_net

# Test rapide sur bridge
Sur bridge on ne peut pas ping via le nom du conteneur mais seulement l'ip. 

# Connecter à chaud un conteneur existant
docker network connect test_net metasploitable

# Puis le déconnecter
docker network disconnect test_net metasploitable

# Et supprimer le réseau
docker network rm test_net





# Questions

- Pourquoi l'utilisation d'un reseau personnalise est-elle recommandee pour des applications multi-conteneurs ?
Un réseau personnalisé est recommandé afin d'avoir un contrôle total dessus. Cela permet d'éviter les connexions non voulues et de pouvoir séparer les conteneurs selon leurs usages. Cela permet également de faire communiquer les machines via leur nom (DNS interne) plutot que leur adresses IP.

- Quel avantage apporte le DNS interne Docker ?
Le DNS interne docker permet de pouvoir faire communiquer les conteneurs via leur nom et non leur adresse IP uniquement. Cela rend plus simples les communications entre eux.

- Que permet `docker network inspect` dans une phase de diagnostic ?
Docker network inspect permet de voir les conteneurs connectés au réseau sélectionné. 