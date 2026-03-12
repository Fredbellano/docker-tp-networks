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
"Name": "app_network",
        "Id": "24c3b0ecc5c8837984fb4a4e6c0799249d1456b83a76d2b2a78984af2157b369",
        "Created": "2026-03-12T14:24:55.645712955Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv4": true,
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
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
        "Containers": {
            "011bca728ff31cd333e7cfd0e77a4d6bb6815bcbdfa58f3a3f43924040126a91": {
                "Name": "webapp",
                "EndpointID": "4f62ad6f40bd3f2d4b5802132c7957d643f9d13272a4fd197a9a3d8836390173",
                "MacAddress": "b2:88:38:ca:64:77",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "c77c7f690aa93dff9c0647da017d47418b2632a3b018fcca819ff2ca2dbf3b0f": {
                "Name": "mysql_db",
                "EndpointID": "8dfdb7dc0060778f871bd44a7def4e6f2c884ef23f4a8aedb460656394878da9",
                "MacAddress": "62:54:02:bc:c4:e8",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
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
|  1 | Sonny |
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
mysql> SELECT * FROM users;
+----+-------+
| id | name  |
+----+-------+
|  1 | Sonny |
+----+-------+
1 row in set (0.001 sec)
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

Questions de reflexion

    - Pourquoi la base de donnees n'a-t-elle pas besoin d'etre exposee vers l'hote dans cette architecture ?
      - Car elle est relié avec le network créé, deplus il n'y a besoin d'accéder à la base de donnée depuis la machine hote comme le nginx
    - En quoi le reseau personnalise simplifie-t-il la communication entre services ?
      - Isolation pour une meilleure communication entre les apps et pas besoin de passer par les ip, mais directement avec le nom du conteneur
    - Que se passerait-il si le volume n'etait pas reutilise apres recreation du conteneur MySQL ?
      - Si le volume n'était pas réutilisé, les données de la base de données seraient perdues. La base serait recréée vide lors du lancement du nouveau conteneur.
