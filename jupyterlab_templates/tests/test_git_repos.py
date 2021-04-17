import json
import os

import requests


def test_server_loaded_notebooks(notebook_server):
    name = "/example-jupyter-notebooks.git/01-MPI-monte-carlo-pi.ipynb"

    resp = requests.get(
        "{}/templates/names".format(notebook_server),
    )
    assert resp.status_code == 200, resp.content
    assert resp.json() == {
        "example-jupyter-notebooks.git": [{"name": name}]
    }

    resp2 = requests.get(
        "{}/templates/get".format(notebook_server), params={"template": name}
    )
    assert resp2.status_code == 200, resp.content
    data = resp2.json()
    assert data["name"] == name
    assert data["dirname"] == "/example-jupyter-notebooks.git"
    assert json.loads(data["content"]) != {}

    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "git-templates", name[1:]))
    assert data["path"] == dir
