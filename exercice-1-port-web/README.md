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

- Quelle est la difference entre le port hote et le port conteneur ? Le port du conteneur sert à dire à la machine hôte sur quel port récupérer les infos du conteneur et le port hôte permet d'exposer e contenu vers l'extérieur
- Pourquoi `EXPOSE` ne suffit-il pas a rendre le service accessible ? Expose permet juste de libérer le port alors que -p permet de mapper le port directement
- Dans quel cas limiter l'ecoute a `127.0.0.1` est-il utile ? Si on travaille en local car seule la machine hôte y a accès

## Criteres de validation

- Le service est accessible sur `http://localhost:8080`
- Les ports publies sont correctement identifies
- La difference entre `EXPOSE` et `-p` est comprise
- Le nettoyage final est realise
