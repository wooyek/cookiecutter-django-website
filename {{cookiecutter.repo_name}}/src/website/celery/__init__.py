# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.

from __future__ import absolute_import

import logging
from celery import Celery, signals


# Using Celery with Django
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django

# set the default Django settings module for the 'celery' program.
from django.conf import settings

# logging.debug("settings.CELERY_ALWAYS_EAGER: %s" % settings.CELERY_ALWAYS_EAGER)

app = Celery('website.celery')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
# logging.debug("app.conf.CELERY_ALWAYS_EAGER: %s" % app.conf.CELERY_ALWAYS_EAGER)

from django.apps import apps
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@signals.after_setup_logger.connect
def augment_logging_cfg(signal=None, sender=None, logger=None, loglevel=None, logfile=None, format=None, colorize=None, *args, **kargs):
    logging.info("Adding AdminEmailHandler to celery loggers")
    from django.utils.log import AdminEmailHandler
    handler = AdminEmailHandler()
    handler.level = logging.ERROR
    logger.handlers.append(handler)
    logging.info("logger.handlers: %s" % logger.handlers)
    logging.info("settings.ADMINS:%s" % settings.ADMINS)


    import sys, os

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


@app.task(bind=True)
def debug_task(self):
    logging.debug("################ : Request: {0!r}".format(self.request))
