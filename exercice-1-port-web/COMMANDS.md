  501  git clone git@github.com:Shogaro/docker-tp-networks.git
  502  cd docker-tp-networks/
  504  cd exercice-1-port-web/
  506  docker run -d --name web-port -p 8080:80 nginx
  507  docker ports web-port
  508  docker ps web-port
  509  docker ps
  510  docker port web-port
  511  git checkout -b Lucas-HENNEBELLE
  512  docker stop web-port
  513  docker remove web-port
  514  docker rm web-port
  515  docker run -d --name web-port -p 127.0.0.1:8080:80 nginx
  516  docker port web-port
  517  docker stop web-port 
  518  docker rm web-port
  519  history > COMMANDS.md
