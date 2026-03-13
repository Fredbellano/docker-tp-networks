[
    {
        "Name": "test_net",
        "Id": "a693f3852f951cdee4151dd43df526434e152397a3cf3b214387ca893b31902c",
        "Created": "2026-03-12T14:09:22.093128723Z",
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
        "Options": {
            "com.docker.network.enable_ipv4": "true",
            "com.docker.network.enable_ipv6": "false"
        },
        "Labels": {},
        "Containers": {
            "746b4ac5ee9fc925f9d77f15932b26f51f5e4e3f5abbe03fd7a3bd92daa633ed": {
                "Name": "serveur",
                "EndpointID": "b3cb3e3abcc4ea410f6e9324c2342471de39c9815d23ca0cc5b51b36891f6eeb",
                "MacAddress": "be:33:80:9f:3a:6a",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Status": {
            "IPAM": {
                "Subnets": {
                    "172.18.0.0/16": {
                        "IPsInUse": 4,
                        "DynamicIPsAvailable": 65532
                    }
                }
            }
        }
    }
]
