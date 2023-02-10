# How to commit if changes done
--------------------------------

`--quiet` flag disables default output of `diff` and implies `--exit-code`.

`--exit-code` flag makes the command exit with 1 if there were differences and 0 otherwise no differences.

```bash
git diff --quiet || (git add README.md && git commit -m "Updated README")
```

This works because in case of an `OR` operator, evaluation of RHS is dependent on the result of RHS. If LHS returns 1, no RHS evaluation.
