# coding=utf-8
# Created 2014 by Janusz Skonieczny

"""
These heavily rely on staging settings and any modifications should consist only of keys and secrets.
Secrets should be loaded of the environment.

The goal here is to not change any settings may have impact on features present.
Changing keys and secrets should not hava that impact.
"""

import logging
import environ
from pathlib import Path
from website import __version__ as release_version
import os

logging.debug("Settings loading: %s" % __file__)

print("###############################")
print("# LOADING PRODUCTION SETTINGS #")
print("###############################")

# Set defaults for when env file is not present.
os.environ.update(DEBUG='False', ASSETS_DEBUG='False')

# This will read missing environment variables from a file
# We want to do this before loading any base settings as they may depend on environment
environ.Env.read_env(str(Path(__file__).parent / "production.env"))

# noinspection PyUnresolvedReferences
from .base import *

LOGGING['handlers']['console']['formatter'] = 'heroku'
LOGGING['handlers']['file'] = {
    'class': 'logging.handlers.RotatingFileHandler',
    'formatter': 'verbose',
    'backupCount': 3,
    'maxBytes': 4194304,  # 4MB
    'level': 'DEBUG',
    'filename': (os.path.join(ROOT_DIR, 'logs', 'website.log')),
}
LOGGING['root']['handlers'].append('file')

log_file = Path(LOGGING['handlers']['file']['filename'])
if not log_file.parent.exists():  # pragma: no cover
    logging.info("Creating log directory: {}".format(log_file.parent))
    Path(log_file).parent.mkdir(parents=True)

