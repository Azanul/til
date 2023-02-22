# How to set namespace
------------------------

Command to set namespace as current
```bash
kubectl config set-context --current --namespace=<target-namespace>
```

Can also access a namespace with the flag `--namespace` like
```bash
kubectl get pods --namespace=<target-namespace>
```
