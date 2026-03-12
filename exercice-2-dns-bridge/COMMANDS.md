docker network create test_net
docker run -d --name serveur --network test_net nginx
docker run --rm -it --network test_net alpine sh
ping serveur sur le serveur alpine
exit
docker network inspect test_net
docker run -d --name nginx_bridge nginx
docker run --rm -it alpine sh
ping nginx_bridge Ne ping pas
docker network connect test_net nginx_bridge
docker run --rm -it --network test_net alpine sh
exit
docker network disconnect test_net nginx_bridgedocker stop serveur nginx_bridge
docker rm serveur nginx_bridge
docker network rm test_net

1) 
Pour la communication entre conteneurs, l'isolement réseau, la gestion claire des services

2) 
Permet de résoudre les noms de conteneurs automatiquement, d'éviter l'utilisation d'IP dynamiques, et de simplifier la configuration des applications

3)
Il permet de voir les conteneurs connectés, leurs adresses IP, les paramètres du réseau et les passerelles et sous-réseaux