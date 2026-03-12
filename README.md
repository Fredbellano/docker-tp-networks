# TP Docker - Gestion des reseaux

Le but est de vous faire pratiquer, pas a pas, l'exposition de ports, la communication entre conteneurs et l'utilisation de reseaux Docker personnalises.

## Objectifs pedagogiques

A la fin du TP, vous devez etre capable de:
- exposer un service vers l'hote avec `-p`
- distinguer `EXPOSE` et publication de ports
- creer et utiliser un reseau Docker personnalise
- verifier la resolution DNS interne par nom de conteneur
- connecter plusieurs conteneurs sur le meme reseau
- combiner reseau et volume dans une architecture simple

## Organisation du TP

Le TP est compose de 3 exercices progressifs:

1. `exercice-1-port-web`
- Exposition d'un serveur web Nginx vers la machine hote
- Focus: `-p`, verification de l'accessibilite, inspection des ports publies

2. `exercice-2-dns-bridge`
- Communication entre conteneurs sur un reseau personnalise
- Focus: `docker network create`, DNS interne, difference bridge par defaut / custom bridge

3. `exercice-3-web-db-network`
- Mini architecture multi-conteneurs avec web, base de donnees, reseau et volume
- Focus: isolation reseau, nommage de services, persistance et verification de bout en bout

## Ce que vous devez rendre

Dans chaque dossier d'exercice, vous devez fournir:
- `README.md` (consigne / contexte / criteres, sans commandes)
- `COMMANDS.md` (toutes les commandes executees pour realiser l'exercice)

Le format attendu est precise dans [CONTRIBUTING.md](./CONTRIBUTING.md).

## Methode de travail conseillee

- Lire d'abord la consigne de l'exercice.
- Realiser un premier test minimal qui fonctionne.
- Verifier l'etat du reseau avec les commandes d'inspection Docker.
- Comparer les comportements selon le type de reseau utilise.
- Documenter vos commandes dans `COMMANDS.md`.

## Evaluation

Vous serez evalues sur:
- la conformite a la consigne
- la bonne utilisation des options reseau Docker
- la capacite a demontrer la communication entre conteneurs
- la maitrise du DNS interne et de l'isolation reseau
- la clarte du rendu

Bon TP.
