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
from pathlib import Path

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
from .components.django_assets import *  # noqa: F402 F403 isort:skip
# from .components.celery import *  # noqa: F402 F403 isort:skip
from .components.import_export import *  # noqa: F402 F403 isort:skip
from .components.pycountry import *  # noqa: F402 F403 isort:skip
from .components.sentry import *  # noqa: F402 F403 isort:skip
from .components.newrelic import *  # noqa: F402 F403 isort:skip
# from .components.django_opt_out import *  # noqa: F402 F403 isort:skip
# from .components.django_email_queue import *  # noqa: F402 F403 isort:skip
# from .components.oauth_toolkit import * # noqa: F402 F403 isort:skip
# from .components.rest_framework import *  # noqa: F402 F403 isort:skip
# from .components.gis import *  # noqa: F402 F403 isort:skip
# from .components.intercom import *  # noqa: F402 F403 isort:skip
from .components.pure_pagination import *  # noqa: F402 F403 isort:skip

# Other imports can cause change in core settings
# we should import core last
from .components.core import env, BASE_DIR  # noqa: F402 F403 isort:skip
from .components.core import *  # noqa: F402 F403 isort:skip

# │ Customizations made for this project only should go bellow
# ╰────────────────────────────────────────────────────────────────────────────


INSTALLED_APPS += (  # noqa: F405
    'bootstrapform',
    # 'django_babel',
    # 'guardian',
    'reversion',
    # 'django_filters',
    'django_powerbank',
    'django_error_views.apps.DjangoErrorViewsConfig',
    # 'localflavor',
    # 'django_gravatar',
    # 'misc.choose_language',
    '{{ cookiecutter.package_name }}.apps.{{ cookiecutter.app_config_name }}',
)

# AUTH_USER_MODEL = '{{ cookiecutter.package_name }}.CustomUser'

LANGUAGE_CODE = 'pl'
TIME_ZONE = 'Europe/Warsaw'

# https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
import django_error_views  # noqa F402 isort:skip

LOCALE_PATHS = [
    str(Path(django_error_views.__file__).parent / 'locales'),
    # str(BASE_DIR / 'locales'),
]


SANDBOX = env("SANDBOX", default=True, cast=bool)