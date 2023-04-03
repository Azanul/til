# How to forward incoming requests to a container port to host port
---------------------------------------------------------------------

socat works by creating a pair of bidirectional streams, each connected to one endpoint, 
and relaying data between them. This makes it possible to bridge different types of endpoints 
and protocols, and to manipulate data streams in various ways.


forward port at `CONTAINER_IP_ADDRESS`:`CONTAINER_PORT` to host `HOST_PORT`.
```
sudo socat tcp-listen:[HOST_PORT],fork,reuseaddr tcp-connect:[CONTAINER_IP_ADDRESS]:80

```

forward docker container port `CONTAINER_PORT` to host `HOST_PORT`.
```
sudo socat tcp-listen:[HOST_PORT],fork,reuseaddr tcp:host.docker.internal:[CONTAINER_PORT]
```

ref: [socat in shared host dev container](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/docker-from-docker#final-fallback-socat)
