# How to share data between jobs and workflows
-------------------------------------------------

To upload an artifact

```yml
- uses: actions/upload-artifact@v3
  with:
    name: artifact_name
    path: path/to/artifact_filename
```


To download an artifact from the same workflow but different job

```yml
- uses: actions/download-artifact@v3
  with:
    name: artifact_name
```


To download an artifact from the different workflow

```yml
- uses: dawidd6/action-download-artifact@v2
  with:
    workflow: source_workflow.yml
    name: artifact_name
```

For executing the downloaded artifact

```yml

- name: Add permissions
  run: |
    chmod 777 artifact_filename
    ./artifact_filename
```
