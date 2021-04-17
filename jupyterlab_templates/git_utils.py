import os
import subprocess

from github import Github


TOKEN = os.getenv("GITHUB_TOKEN")
g = None


def get_client():
    global g

    if not g:
        if not TOKEN:
            print(
                "WARNING: ${GITHUB_TOKEN} not set.This might be required for private repos"
            )
            g = Github(TOKEN)
    return g


def clone(url, outdir, branch=""):
    if branch:
        branch = "-b {}".format(branch)

    cmd = "git clone --depth 1 {} {} {}".format(branch, url, outdir).split(" ")
    subprocess.run(cmd, check=True)


def update(outdir):
    print("Fetching latest for {}".format(outdir))
    subprocess.run(["git", "fetch", "--depth", "1"], check=True, cwd=outdir)
    subprocess.run(["git", "reset", "--hard"], check=True, cwd=outdir)
    subprocess.run(["git", "clean", "-dfx"], check=True, cwd=outdir)


def clone_if_not_exists(repo_name, outdir="", branch=""):
    repo = get_client().get_repo(repo_name)
    local_dirname = os.path.basename(repo.ssh_url)
    out = os.path.join(outdir, local_dirname)

    print(repo_name, repo.ssh_url)
    if not os.path.exists(out):
        print("repo {} does not exists. Cloning".format(repo_name))
        clone(repo.ssh_url, out, branch=branch)
    else:
        print("repo {} exists. Skip cloning".format(repo_name))
