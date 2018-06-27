# coding=utf-8
"""
Django settings for this website project.

Generated by wooyek/cookiecutter-django-website

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

# Before go-live check if your settings are suitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
"""

from __future__ import absolute_import, unicode_literals

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-7s %(thread)-5d %(filename)s:%(lineno)s | %(funcName)s | %(message)s', datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)
logging.disable(logging.NOTSET)

logging.debug("Settings loading: %s" % __file__)

# ╭────────────────────────────────────────────────────────────────────────────
# │ This is a composite strategy for setting up django website instance.
# │ We import default component settings and customise them below in this file
# │ To disable or enable particular component just comment or uncomment a component import

# noinspection PyUnresolvedReferences
from .components.debug_toolbar import *  # noqa: F402 F403 isort:skip
from .components.django_assets import * # noqa: F402 F402
# from .components.celery import * # noqa: F402
# from .components.oauth_toolkit import * # noqa: F402
# from .components.rest_framework import *  # noqa: F402
# from .components.gis import * # noqa: F402
# from .components.intercom import * # noqa: F402

# Other imports can cause change in core settings
# we should import core last
from .components.core import *  # noqa: F402 F403 isort:skip

# │ Customizations made for this project only should go bellow
# ╰────────────────────────────────────────────────────────────────────────────


INSTALLED_APPS += (  # noqa: F405
    # 'bootstrapform',
    # 'django_babel',
    # 'guardian',
    # 'reversion',
    # 'django_filters',
    'django_powerbank',
    'django_error_views.apps.DjangoErrorViewsConfig',
    # 'localflavor',
    # 'django_gravatar',
    # 'misc.choose_language',
    '{{ cookiecutter.package_name }}.apps.PelikanConfig',
)

LANGUAGE_CODE = 'pl'
