# Exercice 2 - DNS interne sur un reseau personnalise

Objectif: comparer le reseau `bridge` par defaut avec un reseau personnalise et verifier la resolution DNS par nom de conteneur.

## Contexte

Deux conteneurs doivent communiquer entre eux. Sur le reseau `bridge` par defaut, cette communication est moins pratique. Sur un reseau personnalise, Docker fournit une resolution DNS interne.

## Travail a faire

1. Creer un reseau Docker personnalise nomme `test_net`.
2. Lancer un conteneur `nginx` nomme `serveur` connecte a ce reseau.
3. Depuis un conteneur ephemere `alpine` connecte au meme reseau, verifier que le nom `serveur` est resolu et joignable.
4. Inspecter le reseau pour identifier les conteneurs connectes.
5. Refaire un test rapide sur le reseau `bridge` par defaut et noter la difference d'usage.
6. Connecter a chaud un conteneur existant a `test_net`.
7. Deconnecter ce conteneur puis supprimer le reseau apres nettoyage.

Les commandes doivent etre fournies dans un fichier separe `COMMANDS.md`.

## Questions de reflexion

- Pourquoi l'utilisation d'un reseau personnalise est-elle recommandee pour des applications multi-conteneurs ?
    Parce que les conteneurs peuvent communiquer plus facilement entre eux sur le même réseau

- Quel avantage apporte le DNS interne Docker ?
    Il permet d’utiliser directement le nom du conteneur pour communiquer, sans avoir besoin de connaître son adresse IP

- Que permet `docker network inspect` dans une phase de diagnostic ?
    `docker network inspect` permet de voir les conteneurs connectés au réseau et leurs informations (par exemple, leur adresse IP)

## Criteres de validation

- Le reseau `test_net` est cree puis supprime proprement
- Le conteneur `serveur` est joignable par son nom depuis un autre conteneur
- L'inspection du reseau montre les conteneurs attendus
- La difference entre `bridge` par defaut et reseau personnalise est explicitement constatee
