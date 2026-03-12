# Exercice 1 - Exposer un service web

Objectif: publier un port de conteneur vers la machine hote et verifier qu'un service web est accessible depuis l'exterieur.

## Contexte

Vous disposez d'un serveur Nginx qui ecoute dans le conteneur sur le port `80`.
Vous devez le rendre accessible depuis votre machine sur un port different et observer la publication des ports.

## Travail a faire

1. Lancer un conteneur `nginx` nomme `web-port`.
2. Publier le port `80` du conteneur sur le port `8080` de la machine hote.
3. Verifier que le service repond sur `http://localhost:8080`.
4. Afficher les ports publies du conteneur.
5. Relancer le meme service avec une publication restreinte a `127.0.0.1`.
6. Comparer ce que vous observez avec une simple declaration `EXPOSE` dans une image.
7. Nettoyer les conteneurs utilises.

Les commandes doivent etre fournies dans un fichier separe `COMMANDS.md`.

## Questions de reflexion

- Quelle est la difference entre le port hote et le port conteneur ?
Le port conteneur est  service à l'intérieur,le port hôte est un port de la machine mappé vers le conteneur.

- Pourquoi `EXPOSE` ne suffit-il pas a rendre le service accessible ?
EXPOSE est documentaire, il faut `-p`/`--publish` pour créer le mapping hôte vers un conteneur.

- Dans quel cas limiter l'ecoute a `127.0.0.1` est-il utile ?
Quand on veut restreindre l'accès au host uniquement (développement, sécurité sur un hôte partagé).

## Criteres de validation

- Le service est accessible sur `http://localhost:8080`
- Les ports publies sont correctement identifies
- La difference entre `EXPOSE` et `-p` est comprise
- Le nettoyage final est realise
