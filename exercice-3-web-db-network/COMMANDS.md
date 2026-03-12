# Commandes

```bash
# Variables (modifiable si besoin)
ROOT_PASS=rootpass
DB_NAME=demo_db
DB_USER=demo_user
DB_PASS=demo_pass

docker network create app_network
docker volume create db_volume
docker run -d --name mysql_db --network app_network \
  -e MYSQL_ROOT_PASSWORD=${ROOT_PASS} \
  -e MYSQL_DATABASE=${DB_NAME} \
  -e MYSQL_USER=${DB_USER} \
  -e MYSQL_PASSWORD=${DB_PASS} \
  -v db_volume:/var/lib/mysql \
  mysql:8
echo "Waiting for mysql to be ready..."
until docker exec mysql_db mysqladmin ping -h localhost -uroot -p${ROOT_PASS} --silent; do sleep 1; done
echo "mysql ready"
docker build -t webapp-image ./webapp
docker run -d --name webapp --network app_network -p 8080:8080 \
  -e DB_HOST=mysql_db -e DB_USER=${DB_USER} -e DB_PASSWORD=${DB_PASS} -e DB_NAME=${DB_NAME} \
  webapp-image
docker network inspect app_network --format "{{json .Containers}}"
curl -sI http://localhost:8080 | head -n 5
curl -s http://localhost:8080/init
curl -s http://localhost:8080/show
docker rm -f mysql_db
docker run -d --name mysql_db --network app_network \
  -e MYSQL_ROOT_PASSWORD=${ROOT_PASS} \
  -e MYSQL_DATABASE=${DB_NAME} \
  -e MYSQL_USER=${DB_USER} \
  -e MYSQL_PASSWORD=${DB_PASS} \
  -v db_volume:/var/lib/mysql \
  mysql:8
echo "Waiting for mysql (recreated) to be ready..."
until docker exec mysql_db mysqladmin ping -h localhost -uroot -p${ROOT_PASS} --silent; do sleep 1; done
echo "mysql recreated and ready"
curl -s http://localhost:8080/show
docker rm -f webapp mysql_db || true
docker network rm app_network || true
docker volume rm db_volume || true
docker rmi webapp-image || true

```