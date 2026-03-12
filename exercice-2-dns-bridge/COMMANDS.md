# COMMANDS.md

# 1) Creer le reseau personnalise

```bash
docker network create test_net
```

# 2) Lancer un conteneur nginx nomme serveur sur ce reseau

```bash
docker run -d --name serveur --network test_net nginx
```

# 3) Depuis un conteneur ephemere Alpine sur le meme reseau

# Test de resolution du nom

```bash
docker run --rm --network test_net alpine ping -c 3 serveur
```

# Test HTTP vers nginx

```bash
docker run --rm --network test_net alpine sh -c "apk add --no-cache curl >/dev/null && curl http://serveur"
```

# 4) Inspecter le reseau pour voir les conteneurs connectes

```bash
docker network inspect test_net
```

# 5) Test rapide sur le reseau `bridge` par defaut

# Lancer un conteneur nginx sur le bridge par defaut

```bash
docker run -d --name serveur_bridge nginx
```

# Depuis Alpine sur le bridge, tester la resolution par nom

```bash
docker run --rm alpine ping -c 3 serveur_bridge
```

# Difference constatee

Sur le reseau bridge par defaut, la resolution DNS par nom de conteneur n'est pas fournie de la meme facon pour ce cas d'usage. Sur un reseau personnalise, le nom serveur est resolu directement entre conteneurs connectes au meme reseau.

# 6) Connecter a chaud un conteneur existant a test_net

```bash
docker network connect test_net serveur_bridge
```

# Verifier apres connexion

```bash
docker network inspect test_net
```

# Tester de nouveau depuis Alpine

```bash
docker run --rm --network test_net alpine ping -c 3 serveur_bridge
```

# 7) Deconnecter le conteneur puis nettoyer

# Deconnecter serveur_bridge de test_net

```bash
docker network disconnect test_net serveur_bridge
```

# Supprimer les conteneurs

```bash
docker rm -f serveur serveur_bridge
```

# Supprimer le reseau

```bash
docker network rm test_net
```

# Pourquoi un reseau personnalise est recommande pour des applications multi-conteneurs ?

Parce qu'il isole mieux les conteneurs d'une meme application, simplifie leur communication, et permet d'utiliser directement les noms de conteneurs au lieu de rechercher des adresses IP.

# Quel avantage apporte le DNS interne Docker ?

Il permet a un conteneur de joindre un autre conteneur par son nom, ce qui evite d'utiliser des IP qui peuvent changer.

# Que permet docker network inspect dans une phase de diagnostic ?

Il permet de voir les conteneurs connectes a un reseau, leurs adresses IP, leurs alias reseau, et donc de verifier rapidement si le probleme vient du reseau ou du rattachement des conteneurs.
