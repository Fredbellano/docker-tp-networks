1.
Parce que les conteneurs connectés au même réseau Docker personnalisé peuvent communiquer par leur nom. Seul le service web needs d'être exposé pour l'utilisateur. La base de données reste isolée pour la sécurité.

2.
Le réseau personnalisé fournit une résolution DNS automatique par nom de conteneur (mysql_db se résout automatiquement), isolant les services et évitant de mapper les ports internes. C'est plus simple que de gérer les adresses IP et ports manuellement.

3.
Les données seraient perdues. Sans réutiliser le volume, le nouveau conteneur MySQL serait complètement vide. Le volume est ce qui persiste les données au-delà du cycle de vie du conteneur.

