docker network create test_net
docker run -d --name serveur --network test_net nginx
docker run --rm --network test_net alpine sh -c "ping -c 1 serveur && wget -qO- http://serveur"
docker network inspect test_net
docker run -d --name serveur-bridge nginx
docker run --rm alpine sh -c "ping -c 1 serveur-bridge || true"
docker network connect test_net serveur-bridge
docker run --rm --network test_net alpine sh -c "ping -c 1 serveur-bridge"
docker network disconnect test_net serveur-bridge
docker rm -f serveur serveur-bridge
docker network rm test_net


- Un reseau perso c'est mieux pour du multi-conteneurs: c'est plus clean, plus previsible, et ca evite les galeres.
- Le DNS interne te permet d'appeler direct par le nom du conteneur (`serveur`) au lieu de courir apres les IP.
- `docker network inspect` te montre qui est connecte, les IP, les alias, bref tout ce qu'il faut pour debug.
