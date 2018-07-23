# coding=utf-8
"""Website configuration and shared commons package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__copyright__ = "Copyright 2018, {{ cookiecutter.copyright }}"
__maintainer__ = """{{ cookiecutter.full_name }}"""
__credits__ = ["""{{ cookiecutter.full_name }}"""]
__version__ = '0.1.0'
__status__ = "Alpha"
__license__ = "Proprietary"
__date__ = '2018-06-29'


def get_strict_version():
    from distutils.version import StrictVersion
    return StrictVersion(__version__)
