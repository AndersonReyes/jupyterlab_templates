import os
import subprocess
import time

import pytest


ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


@pytest.fixture(scope="function")
def notebook_server():
    logfile = open("/tmp/jupyter_server_logs_pytest.txt", "w")
    config = os.path.join(ROOT, "examples", "jupyter_notebook_config.py")
    cmd = ["jupyter", "lab", "--config", config]
    proc = subprocess.Popen(
        cmd,
        stdout=logfile,
        stderr=logfile,
    )

    # Give the server time to start
    time.sleep(1)
    # Check it started successfully
    try:
        if proc.poll():
            raise Exception("process failed to start")

        yield "http://127.0.0.1:8888"
    finally:
        proc.terminate()
        logfile.write("command: {}".format(str(cmd)))
        logfile.close()
