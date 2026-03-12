# Commandes

```bash
docker network create app_network
docker volume create db_volume
```
```bash
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb mysql
```


```bash
docker run -d --name webapp --network app_network -p 8080:80 nginx
```

```bash
docker network inspect app_network
```
```
[
    {
        "Name": "app_network",
        "Id": "435f25bb1013cb1ff2a4d8d94c19f30fc5c06927df28dee4219716c052b787d1",
        "Created": "2026-03-12T15:02:29.822280876Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv4": true,
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.21.0.0/16",
                    "Gateway": "172.21.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Options": {
            "com.docker.network.enable_ipv4": "true",
            "com.docker.network.enable_ipv6": "false"
        },
        "Labels": {},
        "Containers": {
            "151e4cafb04e5e8beba3aaf4cf20a8b91b5a4777353ff7f9a41a6dfb68537ca6": {
                "Name": "webapp",
                "EndpointID": "8a03fe9122bd69bec10b291040d79904c3733a8532ded0e67233d4e7891825e0",
                "MacAddress": "ea:cd:37:75:76:61",
                "IPv4Address": "172.21.0.3/16",
                "IPv6Address": ""
            },
            "3104e3142c157e15443784daa5e66b37d745cba6739a4d60d5fa502aa73b95ac": {
                "Name": "mysql_db",
                "EndpointID": "1aef2f3b257c2b92f092c7a89b217a27c637d959cb06c93c06407386ef06f3c7",
                "MacAddress": "62:2b:13:87:7e:41",
                "IPv4Address": "172.21.0.2/16",
                "IPv6Address": ""
            }
        },
        "Status": {
            "IPAM": {
                "Subnets": {
                    "172.21.0.0/16": {
                        "IPsInUse": 5,
                        "DynamicIPsAvailable": 65531
                    }
                }
            }
        }
    }
]
```

```bash
docker exec -it mysql_db mysql -uroot -proot testdb
```

```SQL
CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50)
);
```

```SQL
INSERT INTO users (name) VALUES ('Sonny');
```

```SQL
SELECT * FROM users;
```

```
+----+-------+
| id | name  |
+----+-------+
|  1 | Mateo |
+----+-------+
1 row in set (0.001 sec)
```

```bash
docker rm -f mysql_db
```


```bash
docker run -d --name mysql_db --network app_network -v db_volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb mysql
```

```bash
docker exec -it mysql_db mysql -uroot -proot testdb
```

```
SELECT * FROM users;
+----+-------+
| id | name  |
+----+-------+
|  1 | Mateo |
+----+-------+
1 row in set (0.003 sec)
```
```bash
docker rm -f webapp mysql_db
```

```bash
docker network rm app_network
```

```bash
docker volume rm db_volume
```
## Questions de reflexion

- Pourquoi la base de donnees n'a-t-elle pas besoin d'etre exposee vers l'hote dans cette architecture ?
    Elle est reliée avec le network
- En quoi le reseau personnalise simplifie-t-il la communication entre services ?
    Il est isolé donc une meilleure communication entre les app, la communication se fait par le nom des conteneur et pas les ip
- Que se passerait-il si le volume n'etait pas reutilise apres recreation du conteneur MySQL ?
    Les données de la bdd seraient perdus