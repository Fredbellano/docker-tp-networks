  520  cd ../exercice-2-dns-bridge/
  521  docker network create test_net
  523  docker run -d --rm --name serveur --network test_net nginx
  524  docker run --rm --network test_net alpine ping -c 3 serveur
  526  docker network inspect test_net > INSPECT.md
  527  docker network connect test_net e79f7d4f49142850c0476775c3e895a01cafe76bce940bd0a5d1824e98d7b543
  533  docker network disconnect test_net serveur
  528  docker stop serveur 
  531  docker network rm test_net 
  534  history > COMMANDS.md
