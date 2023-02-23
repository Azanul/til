# Important extension development commands
---------------------------------------------

To forward ui from a dev server to a docker desktop extension
```bash
docker extension dev ui-source docker-repo/docker-extension:tag http://localhost:3000
```

To enable dev tools in docker desktop for an extension
```bash
docker extension dev debug docker-repo/docker-extension:tag
```
