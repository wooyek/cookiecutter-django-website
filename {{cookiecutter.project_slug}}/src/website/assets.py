# coding=utf-8
# Copyright 2014 Janusz Skonieczny

from os.path import normcase

CSS = (
    "assets/css/bootstrap.css",
    "assets/css/font-awesome.css",
    "assets/css/screen.css",
)

JS = (
    "assets/js/jquery.js",
    "assets/js/bootstrap.js",
    "assets/js/main.js",
)

import sys

if sys.platform == 'win32':
    JS = [normcase(f) for f in JS]
    # IE_JS = [normcase(f) for f in IE_JS]
    CSS = [normcase(f) for f in CSS]

from django_assets import Bundle, register

register('js', Bundle(*JS, filters='yui_js', output='script.%(version)s.js'))
register('css', Bundle(*CSS, filters='yui_css', output='style.%(version)s.css'))
