# Commandes

```bash
# 1) Creer le reseau personnalise
docker network create test_net

# 2) Lancer un serveur nginx sur ce reseau
docker run -d --name serveur --network test_net nginx

# 3) Depuis un conteneur ephemere sur le meme reseau, resoudre et joindre "serveur"
docker run --rm --network test_net alpine sh -c "apk add --no-cache bind-tools curl >/dev/null && nslookup serveur && curl -I http://serveur"

# 4) Inspecter le reseau
docker network inspect test_net

# 5) Comparer avec le bridge par defaut
docker run -d --name serveur-bridge nginx
docker run --rm alpine sh -c "apk add --no-cache bind-tools >/dev/null && nslookup serveur-bridge || true"

# 6) Connecter a chaud un conteneur existant a test_net
docker run -d --name client-bridge alpine sleep 300
docker network connect test_net client-bridge
docker exec client-bridge ping -c 2 serveur

# 7) Deconnecter et nettoyer
docker network disconnect test_net client-bridge
docker rm -f serveur serveur-bridge client-bridge
docker network rm test_net
```

## Reponses aux questions de reflexion

1. Pourquoi un reseau personnalise est recommande:
Il offre une isolation logique claire entre services d'une meme application, une gestion explicite des conteneurs connectes, et un comportement plus previsible qu'un usage implicite du bridge par defaut.

2. Avantage du DNS interne Docker:
Les conteneurs peuvent se joindre par nom (ex: serveur) sans gerer manuellement les adresses IP, ce qui simplifie la communication et evite les erreurs lors des recreations de conteneurs.

3. Interet de docker network inspect en diagnostic:
La commande permet de verifier les conteneurs connectes, leurs adresses IP, les aliases DNS et la configuration reseau, ce qui aide a identifier rapidement les problemes de connectivite.
