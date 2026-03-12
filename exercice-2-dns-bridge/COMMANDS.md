# Commandes

```bash
docker network create test_net
docker run -d --name serveur --network test_net nginx
docker run --rm --network test_net alpine sh -c "ping -c1 serveur && echo 'serveur reachable' || echo 'serveur unreachable'"
docker network inspect test_net
docker run --rm --network bridge alpine sh -c "ping -c1 serveur && echo 'bridge: reachable' || echo 'bridge: unreachable'"
docker run -d --name client --network bridge alpine sleep 300
docker exec client sh -c "ping -c1 serveur && echo 'client before connect: reachable' || echo 'client before connect: unreachable'"
docker network connect test_net client
docker exec client sh -c "ping -c1 serveur && echo 'client after connect: reachable' || echo 'client after connect: unreachable'"
docker network disconnect test_net client || true
docker rm -f client serveur || true
docker network rm test_net || true

```
