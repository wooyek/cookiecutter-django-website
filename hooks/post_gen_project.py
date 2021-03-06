#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
import shutil
import sys
from subprocess import call

import six

BANNER = """ 
 ╭────────────────────────────────────────────────────────────────────────────
 │ Hi {{ cookiecutter.repo_username }}, 
 │  
 │ as you probably know, creating and maintaining any open source is a massive 
 │ amount of free work. So please spread the word, star any project you use 
 │ and say thank's to it's authors on twitter.
 │ 
 │ Thx, @wooyek
 │ https://github.com/wooyek
 ╰────────────────────────────────────────────────────────────────────────────
"""

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
CREATE_VIRTUAL_ENVIRONMENT = '{{ cookiecutter.create_virtual_environment }}'.lower() == 'y'
REPO_URL = "{{ cookiecutter.repo_url }}"
INCLUDE_SPHINX_DOC = '{{ cookiecutter.include_sphinx_doc }}' != 'y'
GIT_INIT = '{{ cookiecutter.git_init }}'.lower() == 'y'
RUN_TESTS = '{{ cookiecutter.run_tests_on_init }}' == 'y'
INCLUDE_SPHINX = '{{ cookiecutter.include_sphinx_doc }}' == 'y'

try:
    from shutil import which as shutil_which
except ImportError:
    from backports.shutil_which import which as shutil_which

VEX_AVAILABLE = shutil_which('vex')
PEW_AVAILABLE = shutil_which('pew')
PIPENV_AVAILABLE = shutil_which('pipenv')


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def bootstrap_venv():
    # On Windows  current python3 may just be python or not available from PATH
    python = sys.executable or 'python3'
    if PEW_AVAILABLE:
        bootstrap_pew(python)
        return

    if six.PY2:
        print("-------> VirtualEnv: Bootstrapping virtual environment")
        call(["virtualenv", "--clear", ".pyvenv"])
    else:
        print("-------> PyVenv: Bootstrapping virtual environment")
        call([python, "-m", "venv", "--clear", ".pyvenv"])

    venv_py = ".pyvenv/Scripts/python" if platform.system() == "Windows" else ".pyvenv/bin/python"
    call([venv_py, "-m", "pip", "install", "-U", "pip", "setuptools"])
    call([venv_py, "-m", "pip", "install", "-r", "requirements/development.txt"])
    call([venv_py, "-m", "pip", "install", "-e", "."])


def bootstrap_pew(python):
    print("-------> Python Env Wrapper: Bootstrapping virtual environment")
    # delegate all the work to the pew tool
    call((
        "pew", 'new',
        "--python", python,
        '-a', PROJECT_DIRECTORY,
        '-i', 'setuptools',
        '-r', 'requirements/development.txt',
        '--dont-activate',
        '{{ cookiecutter.project_slug }}'
    ))
    # Editable installs are done from requirements
    # call(["pew", "in", PROJECT_SLUG, "pip", "-e", "."])


def git_init():
    print("-------> Initializing git repo")
    call(["git", "init"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-am", "init"])
    call(["git", "flow", "init", "-d"])
    call(["git", "remote", "add", "origin", REPO_URL])


if __name__ == '__main__':

    if CREATE_VIRTUAL_ENVIRONMENT:
        bootstrap_venv()
        if INCLUDE_SPHINX:
            if VEX_AVAILABLE:
                print("-------> Building documentation through vex + make")
                call(["vex", PROJECT_SLUG, "make", "docs"])
            else:
                # TODO: Activate pyvenv before running make
                call(["make", "docs"])

    if INCLUDE_SPHINX_DOC:
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'docs'))

    if CREATE_VIRTUAL_ENVIRONMENT and VEX_AVAILABLE and PIPENV_AVAILABLE:
        call(["vex", PROJECT_SLUG, 'pipenv', 'install', '-r', 'requirements/production.txt'])
        call(["vex", PROJECT_SLUG, 'pipenv', 'install', '--dev', '-r', 'requirements/development.txt'])

    if GIT_INIT:
        git_init()

    if RUN_TESTS:
        print("-------> Running tests")
        # call(["detox", "--skip-missing-interpreters"])
        # call(["detox", "--skip-missing-interpreters", "-e", "clean,py35-django-111,check,report,docs,spell"])
        # call(["make", "test"])
        call(["make", "tox"])

    print(BANNER)
    if CREATE_VIRTUAL_ENVIRONMENT and VEX_AVAILABLE and not os.environ.get('TRAVIS', None):
        call(["vex", PROJECT_SLUG])
