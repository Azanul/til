# How to fix insufficient permission error
-------------------------------------------

Error
```bash
    error: insufficient permission for adding an object to repository database     .git/objects

    fatal: failed to write object
    fatal: unpack-objects failed
```
This error comes because of a mistaken `sudo` command for any git operation.

Resolution
```bash
sudo chown -R $(id -u):$(id -g) "$(git rev-parse --show-toplevel)/.git"
```

ref: [STO issue](https://stackoverflow.com/questions/18779442/error-while-pull-from-git-insufficient-permission-for-adding-an-object-to-repo)
