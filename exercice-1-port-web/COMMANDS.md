# Commandes

```bash
docker run -d --name web-port -p 8080:80 nginx                                                                                                                                              
docker port web-port                                                                                                                                                                        
 # 80/tcp -> 0.0.0.0:8080
 # 80/tcp -> [::]:8080
docker run -d -p 127.0.0.1:8080:80 nginx
 # Le EXPOSE décrit quel port doit être utilisé pour le conteneur, la commande le lance concrétement
docker rm -f web-port 
```

Questions de reflexion
Quelle est la difference entre le port hote et le port conteneur ?
Pourquoi EXPOSE ne suffit-il pas a rendre le service accessible ?
Dans quel cas limiter l'ecoute a 127.0.0.1 est-il utile ?

- le port hote correspond à celui de la machine, le port conteneur est le port du conteneur par lequel on va passer pour accèder à celui ci
- expose est juste un einstruction à l'utilisateur ce n'est pas une commande
- pour isoler le conteneur des autres 