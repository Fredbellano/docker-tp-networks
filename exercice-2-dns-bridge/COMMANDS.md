# Commandes

```bash
docker network create test_net
```


```bash
docker run -d --name serveur --network test_net -p 8080:80 nginx 
```


```bash
docker run -it --rm --name ephemere --network test_net alpine
```

```bash
/$ ping serveur
PING serveur (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.176 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.165 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.170 ms
64 bytes from 172.18.0.2: seq=3 ttl=64 time=0.155 ms
64 bytes from 172.18.0.2: seq=4 ttl=64 time=0.193 ms
64 bytes from 172.18.0.2: seq=5 ttl=64 time=0.113 ms
64 bytes from 172.18.0.2: seq=6 ttl=64 time=0.172 ms

64 bytes from 172.18.0.2: seq=7 ttl=64 time=0.186 ms
^C
--- serveur ping statistics ---
8 packets transmitted, 8 packets received, 0% packet loss
round-trip min/avg/max = 0.113/0.166/0.193 ms
```

```bash
docker network inspect test_net
```

```
"Name": "test_net",
        "Id": "14d9f595942aae2a0eb02066eaf0bde872ef4e23a44ee1edd66a9695463bd6a8",
        "Created": "2026-03-12T13:57:55.454794508Z",
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
            "c7fd82affb15019898f74ca31d8c4d2dd6a30479fa4b781d861b9da17d57175d": {
                "Name": "ephemere",
                "EndpointID": "fd88e01694ee057ff1978fc71d117c3a3a0297b710401195d572f68ca491c68b",
                "MacAddress": "86:81:db:30:ce:f7",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "d7fc243f0a8fcc8916a5f796ac50f6bfd864bf20d3005d07e3cb9efc8cd1793a": {
                "Name": "serveur",
                "EndpointID": "5f3f29a3ef50fe1c0a46622990871b33b9aadd07a17dd73d9acc312986e5a52b",
                "MacAddress": "be:5e:91:61:90:59",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
```

```bash
docker rm -f serveur
```

```bash
docker run -d --name serveur  -p 8080:80 nginx 
```


```bash
docker run -it --rm --name ephemere alpine
```

```bash
/$ ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.301 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.160 ms
64 bytes from 172.17.0.2: seq=2 ttl=64 time=0.188 ms
64 bytes from 172.17.0.2: seq=3 ttl=64 time=0.166 ms
64 bytes from 172.17.0.2: seq=4 ttl=64 time=0.168 ms
64 bytes from 172.17.0.2: seq=5 ttl=64 time=0.164 ms
^C
--- 172.17.0.2 ping statistics ---
6 packets transmitted, 6 packets received, 0% packet loss
round-trip min/avg/max = 0.160/0.191/0.301 ms
```

- On est dans l'incapacité de ping sur le nom du conteneur mais uniquement via l'IP que j'ai récupérer en faisant un 
```bash
docker network inspect bridge
```

```bash
docker network connect test_net serveur
```

```bash 
docker network disconnect test_net serveur
```

```bash
docker network rm test_net
```

Questions de reflexion:

    - Pourquoi l'utilisation d'un reseau personnalise est-elle recommandee pour des applications multi-conteneurs ?
        - Pour créer un cluster dans le sens ou ils sont isolé d'autre conteneur potentiellement UP
    - Quel avantage apporte le DNS interne Docker ?
        - Il est possible de ping le nom du conteneur et non avec l'ip
    -Que permet docker network inspect dans une phase de diagnostic ?
        - savoir a quel réseau est connecté quel conteneur.
