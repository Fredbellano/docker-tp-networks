  535  cd ../exercice-3-web-db-network/
  536  clear
  537  docker network create app_network
  538  volume create --name db_volum
  539  docker volume create --name db_volume
  540  docker run -d --name mysql_db --network app_network -v db_volume:/data
  541  docker run -d --name mysql_db --network app_network -v db_volume:/data mysql
  542  docker run -d --name webapp --network app_network -p 8080:80 nginx
  543  docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql mysql:8
  544  docker network inspect app_network 
  545  docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=true -v db_volume:/var/lib/mysql mysql:8
  546  docker network inspect app_network 
  547  docker exec -ti mysql_db mysql -p appdb
  548  docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -v db_volume:/var/lib/mysql mysql:8
  549  docker exec -i mysql_db mysql -uroot -proot exodb "CREATE TABLE IF NOT EXISTS test(id INT AUTO_INCREMENT, message VARCHAR(255));"
  550  docker exec -i mysql_db mysql -uroot -proot exodb "INSERT INTO test(message) VALUES('test message')"
  551  docker exec -i mysql_db mysql -uroot -proot exodb "SELECT * FROM test"
  552  docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -v db_volume:/var/lib/mysql mysql:8
  553  docker exec -i mysql_db mysql -uroot -proot exodb "CREATE TABLE IF NOT EXISTS test(id INT AUTO_INCREMENT, message VARCHAR(255));"
  554  docker exec -i mysql_db mysql -uroot -proot testdb -e "CREATE TABLE IF NOT EXISTS test(id INT AUTO_INCREMENT, message VARCHAR(255));"
  555  clear
  556  docker run -d --name mysql_db --network app_network -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=ts -v db_volume:/var/lib/mysql mysql:8
  557  docker exec -it mysql_db mysql -p ts
  558  docker exec -it mysql_db mysql -uroot -proot ts
  559  docker run -d --name mysql_db --network app_network -e MYSQL_DATABASE=ts -v db_volume:/var/lib/mysql mysql:8
  560  docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql mysql:8
  561  docker run -d --name mysql_db --network app_network -e MYSQL_ALLOW_EMPTY_PASSWORD  -v db_volume:/var/lib/mysql mysql:8
  562  docker run -d --name mysql_db --network app_network -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v db_volume:/var/lib/mysql mysql:8
  563  docker exec -it mysql_db sh
  564  docker exec -it mysql_db mysql
  565  docker exec -it mysql_db mysql "CREATE DATABASE test"
  566  docker exec -it mysql_db mysql 
  567  docker run -d --name mysql_db --network app_network -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v db_volume:/var/lib/mysql mysql:8
  568  docker run -d --name mysql_db --network app_network -e MYSQL_ALLOW_EMPTY_PASSWORD=true -e MYSQL_DATABASE=test -v db_volume:/var/lib/mysql mysql:8
  569  docker exec -i mysql_db mysql test -e "CREATE TABLE IF NOT EXISTS notes(id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255));"
  570  docker exec -i mysql_db mysql test -e "INSERT INTO notes(message) VALUE('Un message');"
  571  docker rm -f mysql_db
  572  docker run -d --name mysql_db --network app_network -e MYSQL_ALLOW_EMPTY_PASSWORD=true -e MYSQL_DATABASE=test -v db_volume:/var/lib/mysql mysql:8
  573  docker exec -i mysql_db mysql test -e "SELECT * FROM test;"
  574  docker rm -f webapp mysql_db
  575  docker network rm app_network
  576  docker volume rm db_volume
  577  history > COMMANDS.md 
