# Commandes

```bash
# Exemple de structure attendue
docker network create test_net
```

```bash
docker network create test_net
docker run -d --name serveur --network test_net nginx
docker run --rm --network test_net alpine ping -c 3 serveur 
docker network inspect test_net 
# on peut ping depusi le bridge alors qu'il faut une commande avec le réseau créer
docker run --name test2 alpine & docker network connect test_net test2   
docker network disconnect test_net test2 & docker network disconnect test_net serveur  & docker network rm test_net test_net
```
Questions de reflexion
Pourquoi l'utilisation d'un reseau personnalise est-elle recommandee pour des applications multi-conteneurs ?
Quel avantage apporte le DNS interne Docker ?
Que permet docker network inspect dans une phase de diagnostic ?

- un réseau personnalisé permet de mieux gérer la communication entre plusieurs conteneurs 
- le DNS interne permet à des conteneurs de communiquer simplement par leur nom
- elle permet de voir directement lesinformations précises du réseau