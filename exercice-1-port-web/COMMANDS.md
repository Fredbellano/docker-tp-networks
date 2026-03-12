docker run -d --name web-port -p 8080:80 nginx
curl http://localhost:8080
docker port web-port
docker rm -f web-port
docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
docker inspect -f "{{json .Config.ExposedPorts}} {{json .NetworkSettings.Ports}}" web-port
docker rm -f web-port


- Le port conteneur c'est le port dans le conteneur (ex: 80), le port hote c'est celui de ton PC (ex: 8080).
- `EXPOSE` juste "annonce" le port, mais ca l'ouvre pas vers l'exterieur. Pour vraiment publier faut `-p`.
- `127.0.0.1` c'est utile quand tu veux que ca reste local a ta machine (pas accessible depuis le reseau).
