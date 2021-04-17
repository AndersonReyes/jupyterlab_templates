# For pytest only, do not use in production
c.NotebookApp.token = ''
c.NotebookApp.password = ''

## Templates
c.JupyterLabTemplates.include_default = False
c.JupyterLabTemplates.include_core_paths = False
c.JupyterLabTemplates.git_repos = {
    "NERSC/example-jupyter-notebooks": "master"
}
