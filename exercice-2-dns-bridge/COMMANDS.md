# Commandes

```bash
# Création du réseau personnalisé
docker network create test_net

# Lancement du serveur Nginx sur le nouveau réseau
docker run -d --name serveur --network test_net nginx

# Vérification par ping depuis un conteneur éphémère
docker run --rm --network test_net alpine ping -c 2 serveur
# Le ping fonctionne

# Vérification par requête HTTP
docker run --rm --network test_net alpine wget -qO- serveur
# La requete fonctionne

#Inspection du réseau pour identifier les conteneurs connectés
docker network inspect test_net

# Lancement sur le pont par défaut
docker run -d --name serveur-bridge nginx

# Tentative de ping 
docker run --rm alpine ping -c 2 serveur-bridge
#Pas de réponse

# Lancement d'un conteneur isolé
docker run -d --name passager alpine sleep 1000

# Connexion au réseau test_net en cours d'exécution
docker network connect test_net passager

# Vérification de la connectivité vers 'serveur'
docker exec passager ping -c 2 serveur
# Le ping fonctionne

# Déconnexion et nettoyage
docker network disconnect test_net passager

docker rm -f serveur serveur-bridge passager
docker network rm test_net
```

1) Les réseaux personnalisés assurent l'isolation des flux applicatifs et activent la découverte automatique des services par noms d'hôtes, contrairement au pont par défaut.

2) Le DNS interne permet une communication résiliente via des noms logiques immuables, supprimant la dépendance aux adresses IP éphémères des conteneurs.

3) L'inspection réseau permet de valider la configuration des sous-réseaux, d'identifier les conflits d'adresses IP et de confirmer l'adhésion des conteneurs aux segments réseau.
