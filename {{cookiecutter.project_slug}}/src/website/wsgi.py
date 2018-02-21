"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# This will help debug things in the gunicorn environment

print("Importing: %s" % __file__)

import logging
import os
import sys

logging.basicConfig(format='%(asctime)s %(levelname)-7s %(thread)-5d %(filename)s:%(lineno)s | %(funcName)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)
logging.disable(logging.NOTSET)
logging.info('Loading %s', __name__)

DJANGO_SETTINGS_MODULE = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
print("DJANGO_SETTINGS_MODULE=", DJANGO_SETTINGS_MODULE)
from django.conf import settings

# determine where is the single absolute path that
# will be used as a reference point for other directories
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
logging.debug("SITE_ROOT: %s" % SITE_ROOT)
logging.debug("settings.DEBUG: %s" % settings.DEBUG)

# Obtain WSGIHandler
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

application = get_wsgi_application()
application = Sentry(application)
application = DjangoWhiteNoise(application)

logging.debug("application: %s" % application)
