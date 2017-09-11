# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.

"""
These should mimic a production settings making minimal modifications to accommodate tests
"""

import logging
import os
import environ
from pathlib import Path

logging.basicConfig(format='%(asctime)s %(levelname)-7s %(thread)-5d %(filename)s:%(lineno)s | %(funcName)s | %(message)s', datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)
logging.disable(logging.NOTSET)
logging.getLogger('environ').setLevel(logging.INFO)

logging.debug("Settings loading: %s" % __file__)

SETTINGS_FOLDER = Path(__file__).parent.resolve()

# Set defaults for when env file is not present.
# These need to be entered into an environment,
# for django settings (or anything else) to load it from there
# It may or may not be overridden by read_env below.
os.environ.update(
    DEBUG='False',
    ASSETS_DEBUG='False',
    GOOGLE_APPLICATION_CREDENTIALS=str(SETTINGS_FOLDER / "Testing Your-HR-0a3f150f7ca0.json"),
)

# This will read missing environment variables from a file
# We want to do this before loading any base settings as they may depend on environment
environ.Env.read_env(str(SETTINGS_FOLDER / "testing.env"))

# noinspection PyUnresolvedReferences
from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGGING['handlers']['mail_admins']['email_backend'] = 'django.core.mail.backends.dummy.EmailBackend'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# The name of the class to use to run the test suite
TEST_RUNNER = 'misc.testing.KeepDbTestRunner'

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
TASKER_ALWAYS_EAGER = True

