"""
Does the following:
# 1. Removes the example project if it isn't going to be used
"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_example_project():
    location = os.path.join(
        PROJECT_DIRECTORY,
        'example_project'
    )
    shutil.rmtree(location)


if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
    remove_example_project()


def boostrap_venv():
    print("### Bootstrapping virtual environment")
    from subprocess import call
    call(["python3", "-m", "venv", "--clear", ".pve"])
    call([".pve/bin/pip", "install", "-U", "pip", "setuptools"])


if '{{ cookiecutter.create_virtual_environment }}'.lower() == 'y':
    boostrap_venv()


def git_init():
    print("### Initializing git repo")
    from subprocess import call
    call(["git", "init"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-am", "init"])
    call(["git", "flow", "init"])
    call(["git", "remote", "add", "origin", "git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git"])


if '{{ cookiecutter.git_init }}'.lower() == 'y':
    git_init()
