# Commandes

```bash
# Exemple de structure attendue
docker network create test_net
```
2.
# Lancer un conteneur nginx nommé serveur
docker run -d --name serveur --network test_net nginx

3.
# Verifier le nom seveur est résolu et joignable
docker run --rm --network test_net alpine ping -c 3 serveur

4.
# Inspecter le réseau pour identifier les conteneurs connectés
docker network inspect test_net

5.
# test rapide sur le réseau bridge par défaut
# Lancer un conteneur sur le réseau bridge
docker run -d --name serveur-bridge nginx

# tester depuis un conteneur alpine sur bridge
docker run --rm alpine ping -c 3 serveur-bridge

6.
# Connexter le contneeur server-bridge au réseau test_net 
docker network connect test_net serveur-bridge

# Verfication
docker network inspect test_net


7.
# Deconnecter server-bridge
docker network disconnect test_net serveur-bridge

# Supprimer les conteneurs
docker rm -f serveur serveur-bridge

# Supprimer le réseau
docker network rm test_net