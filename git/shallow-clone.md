# How to shallow clone a git repo
-------------------------------------------------


Provide an argument of -- depth 1 to the git clone command to copy only the latest revision of a repo:

```
git clone -–depth [depth] [remote-url]
```
 

You can also use git shallow clone to access a single branch:

```
git clone [remote-url] --branch [name] --single-branch [folder]
```
