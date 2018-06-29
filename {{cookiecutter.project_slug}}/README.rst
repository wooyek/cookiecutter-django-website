{% set is_open_source = cookiecutter.open_source_license != 'Propertiary' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

{% if cookiecutter.use_travis_ci == 'y' -%}
.. image:: https://img.shields.io/travis/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}
{%- endif %}

{% if cookiecutter.use_read_the_docs == 'y' -%}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}
.. image:: https://coveralls.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/badge.svg?branch=develop
        :target: https://coveralls.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url={{ cookiecutter.project_url }}
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/{{ cookiecutter.repo_username }}

{%- endif %}


{% if is_open_source -%}
* Free software: {{ cookiecutter.open_source_license }}
{%- else -%}
* Propertiary software of {{ cookiecutter.copyright }}, please obtain a license before use.
{%- endif %}
{% if cookiecutter.use_read_the_docs == 'y' -%}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{%- endif %}

Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

1. Fork the `{{ cookiecutter.project_slug }}` repo on bitbucket.org
2. Clone your fork locally::

    $ git clone {{ cookiecutter.repo_url }}

3. Setup your development env::

    $ pipsi install pew
    $ cd {{ cookiecutter.project_slug }}/
    $ pew new -p python3 -a $(pwd) $(pwd | xargs basename)
    $ pew workon {{ cookiecutter.project_slug }}
    $ pip install -r requirements/development.txt

4. Test project health::

    $ python manage.py check
    $ pytest
    $ inv check
    $ tox

5. Initialize development database and fill it with test data::

    $ bash bin/database_create.sh
    $ inv db

6. Create a branch for local development and start development server::

    $ git checkout -b name-of-your-bugfix-or-feature
    $ python manage.py runserver


Deployment
----------

Add a development remote and deploy::

    $ git remote add dev https://git.heroku.com/{{ cookiecutter.project_slug }}-dev.git
    $ inv deploy

Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install
