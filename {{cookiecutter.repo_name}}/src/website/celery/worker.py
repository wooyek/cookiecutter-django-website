# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.

from __future__ import absolute_import

import getpass
import logging
import os

import sys

logging.basicConfig(format='%(asctime)s %(levelname)-7s %(thread)-5d %(filename)s:%(lineno)s | %(funcName)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)
logging.disable(logging.NOTSET)

logging.info("Celery user: %s" % getpass.getuser())

# determine where is the single absolute path that
# will be used as a reference point for other directories
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
logging.info("os.environ['DJANGO_SETTINGS_MODULE']: %s" % os.environ['DJANGO_SETTINGS_MODULE'])

# Show a debugging info on console
logging.debug("__file__ = %s", __file__)
logging.debug("sys.version = %s", sys.version)
logging.debug("os.getpid() = %s", os.getpid())
logging.debug("os.getcwd() = %s", os.getcwd())
logging.debug("os.curdir = %s", os.curdir)
logging.debug("sys.path:\n\t%s", "\n\t".join(sys.path))
logging.debug("PYTHONPATH:\n\t%s", "\n\t".join(os.environ.get('PYTHONPATH', "").split(';')))
logging.debug("sys.modules.keys() = %s", repr(sys.modules.keys()))
logging.debug("sys.modules.has_key('website') = %s", 'website' in sys.modules)
if 'website' in sys.modules:
    logging.debug("sys.modules['website'].__name__ = %s", sys.modules['website'].__name__)
    logging.debug("sys.modules['website'].__file__ = %s", sys.modules['website'].__file__)

from django.conf import settings
import django

django.setup()
logging.debug("settings.__dir__: %s", settings.__dir__())
logging.debug("settings.DEBUG: %s", settings.DEBUG)

# When website.celery.worker is used as a worker app
# Celery will look for app attribute in this module
from website.celery import app

# hack to workaround celery removing cwd from sys.paht
# https://github.com/celery/celery/issues/3150
import dinja2

# from website.logcfg import trace_disabled_loggers
# trace_disabled_loggers()

if __name__ == '__main__':
    from celery import __main__
    __main__.main()
    logging.info("Celery worker exiting...")
