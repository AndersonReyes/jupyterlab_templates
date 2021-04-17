# For pytest only, do not use in production
c.NotebookApp.token = ''
c.NotebookApp.password = ''

## Templates
c.JupyterLabTemplates.include_default = True
c.JupyterLabTemplates.include_core_paths = True
c.JupyterLabTemplates.git_repos = {
    "ibm-et/jupyter-samples": "master",
    "NERSC/example-jupyter-notebooks": "master"
}
