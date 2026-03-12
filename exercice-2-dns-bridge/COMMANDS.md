# Commandes

```bash
# Exemple de structure attendue
docker network create test_net

docker run -d --name serveur --network test_net Nginx

docker run --rm --network test_net alpine ping -c 2 serveur

docker network inspect test_net

docker run -d --name serveur-bridge Nginx

docker run --rm alpine ping -c 2 serveur-bridge

docker network connect test_net serveur-bridge

docker network disconnect test_net serveur-bridge

docker rm -f serveur serveur-bridge

docker network rm test_net

Q1 : 
Pour l'isolation et la résolution de noms

Q2 : 
Il permet aux conteneurs de se parler via leurs noms

Q3 : 
Outil de diagnostic, il permet de voir quels conteneurs sont branchés
```
