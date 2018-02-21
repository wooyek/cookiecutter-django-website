=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

* TODO

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-django-website`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-django-website`: https://github.com/wooyek/cookiecutter-django-website
