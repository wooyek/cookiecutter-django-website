# coding=utf-8
from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as __, ugettext_lazy as _
from django.shortcuts import resolve_url

from misc.mail import send_mail_template
