# coding=utf-8
# Based on https://github.com/wooyek/cookiecutter-django-website by Janusz Skonieczny

import logging
import environ
from pathlib import Path

logging.debug("Settings loading: %s" % __file__)

# This will read missing environment variables from a file
# We want to do this before loading any base settings as they may depend on environment
environ.Env.read_env(str(Path(__file__).parent / "local.env"), DEBUG='True')
from .base import *

# https://docs.djangoproject.com/en/1.6/topics/email/#console-backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
LOGGING['handlers']['mail_admins']['email_backend'] = 'django.core.mail.backends.dummy.EmailBackend'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


