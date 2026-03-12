# Exercice 3 - Architecture web + base de donnees

Objectif: mettre en place une architecture simple composee de plusieurs conteneurs relies par un reseau personnalise, avec persistance des donnees via un volume.

## Contexte

Vous devez reproduire une architecture minimale composee:
- d'un conteneur web `webapp`
- d'un conteneur base de donnees `mysql_db`
- d'un reseau `app_network`
- d'un volume `db_volume`

L'application web doit etre exposee vers l'hote, tandis que la base de donnees doit rester accessible uniquement a l'interieur du reseau Docker.

## Travail a faire

1. Creer un reseau `app_network`.
2. Creer un volume `db_volume`.
3. Lancer un conteneur MySQL `mysql_db` connecte a `app_network` et utilisant `db_volume`.
4. Lancer un conteneur `webapp` connecte au meme reseau et publie sur `http://localhost:8080`.
5. Verifier que `webapp` et `mysql_db` apparaissent bien dans l'inspection du reseau.
6. Inserer une donnee dans la base puis verifier sa presence.
7. Supprimer puis recreer uniquement le conteneur `mysql_db` avec le meme volume.
8. Verifier que la donnee est toujours presente.
9. Nettoyer les conteneurs, le reseau et le volume.

Les commandes doivent etre fournies dans un fichier separe `COMMANDS.md`.

## Questions de reflexion

- Pourquoi la base de donnees n'a-t-elle pas besoin d'etre exposee vers l'hote dans cette architecture ?

Parce que seule le conteneur web doit etre accessible à l'hote

- En quoi le reseau personnalise simplifie-t-il la communication entre services ?

Cela permet aux conteneurs de communiquer directement par leur nom drâce au DNS

- Que se passerait-il si le volume n'etait pas reutilise apres recreation du conteneur MySQL ?

Les données serait perdues. Le conteneur MySQL redémarrerait avec un espace de stockage vide.

## Criteres de validation

- Les conteneurs `webapp` et `mysql_db` partagent bien le reseau `app_network`
- Le service web est accessible sur `http://localhost:8080`
- Les donnees MySQL persistent apres recreation du conteneur
- Le nettoyage final supprime correctement les ressources creees
