# Commandes

```bash
# Exemple de structure attendue
docker network create test_net
```

```bash
docker run -d --name serveur --network test_net nginx
```

```bash
docker run --rm --network test_net alpine ping -c 3 serveur
```

```bash
docker network inspect test_net
```

```bash
docker run -d --name serveur-defaut nginx
docker run --rm alpine ping serveur-defaut
```
On recoit une 'bad adress'

```bash
docker network connect test_net serveur-defaut
```

```bash
docker network disconnect test_net serveur-defaut
docker rm -f serveur serveur-defaut
docker network rm test_net
```