import os
import subprocess
import time

import pytest


ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


@pytest.fixture(scope="function")
def notebook_server():
    config = os.path.join(ROOT, "examples", "gitrepos", "jupyter_notebook_config.py")
    proc = subprocess.Popen(
        [
            "jupyter",
            "lab",
            "--config",
            config
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    # Give the server time to start
    time.sleep(.30)
    # Check it started successfully
    try:
        if proc.poll():
            raise Exception("process failed to start: {}".format(proc.stdout.read()))

        yield "http://127.0.0.1:8888"
    finally:
        proc.terminate()
    # Shut it down at the end of the pytest session
