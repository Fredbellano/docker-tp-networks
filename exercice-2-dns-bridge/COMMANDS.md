# Commandes

```bash
# Exemple de structure attendue
docker network create test_net
```
# 1. Création du réseau test_net

```bash
docker network create test_net
```
# 2. Conteneur `nginx` nomme `serveur` connecte a ce reseau.

```bash
docker run -d --name serveur --network test_net nginx
```

# 3. Depuis un autre conteneur, on pinge "serveur" par son nom

```bash
docker run --rm --network test_net alpine ping -c 3 serveur
```
# 4. Inspecter le reseau pour identifier les conteneurs connectes.

```bash
docker network inspect test_net
```

# --> on a bien le contener serveur connecté au réseau

### 5. Comparaison avec le bridge par défaut
```bash
docker run -d --name serveur_bridge nginx
```
```bash
docker run --rm alpine ping -c 2 serveur_bridge
```
# --> la tentaive de ping échoue le bridge par défault ne supporte pas e DNS



# 6. Connecter a chaud un conteneur existant a `test_net`.

# On test avec le serveur_bridge

```bash
docker network connect test_net serveur_bridge
```

# 7. Deconnecter ce conteneur puis supprimer le reseau apres nettoyage.

```bash
docker network disconnect test_net serveur_bridge
```

```bash
docker network rm mon_reseau
```

## Questions de reflexion

- Pourquoi l'utilisation d'un reseau personnalise est-elle recommandee pour des applications multi-conteneurs ?
    Cela simplifie la communication entre les services
- Quel avantage apporte le DNS interne Docker ?
    Il permet de ne pas utiliser les adresses IP, les conteneurs communiquent entre eux via leurs noms
- Que permet `docker network inspect` dans une phase de diagnostic ?

    Verifier la liste des conteneur connectés à un réseau
    Vérfier les passerelles
    Vérifier leur ip
