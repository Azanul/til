How to remove commits from git history
---------------------------------------

Reset `HEAD` to the last commit that you want to keep. There are three steps to reset:
1. Reset refs: The repo pointer is moved to the passed commit SHA. (`--soft` only does this)
2. Reset stage: The staged files are moved to working directory. (`--mixed` does this too)
3. Reset working directory: The files in the working directory are reset. (`--hard` does all three)

Default: `--mixed`

Then force push.

```shell session
git reset xxxxxxxx9819d19b6cb6185d107c565b4d5ba1d7
git push --force
```
