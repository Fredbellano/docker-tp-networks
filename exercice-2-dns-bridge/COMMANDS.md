# Commandes

```bash
# Exemple de structure attendue
docker network create test_net

docker run -d --name serveur --network test_net nginx

docker run --rm -it --network test_net alpine ping serveur

docker network inspect test_net

docker run -d --name serveur_bridge nginx 
docker run --rm -it alpine ping serveur_bridge #le nom n'est pas résolu

docker network connect test_net serveur_bridge

docker network disconnect test_net serveur_bridge
docker stop serveur serveur_bridge
docker rm serveur serveur_bridge
docker network rm test_net

L'utilisation d'un reseau personnalise est recommandee pour des applications multi-conteneurs car ça permet une isolation réseau, une résolution rapide du DNS via le nom et une communication simple entre coneneur.

Le DNS interne Docker permet d'utiliser le nom du conteneur comme adresse.

`docker network inspect` permet d'inspecter le reseau afin d'identifier les conteneurs connectés et identifié les problèmes de communication réseau.
```
