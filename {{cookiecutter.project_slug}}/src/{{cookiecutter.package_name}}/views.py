import logging
from collections import OrderedDict

from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, resolve_url
from django.urls import reverse
from django.utils import timezone
from django.utils.http import urlencode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import ProcessFormView, FormMixin
from django_powerbank.views import Http401, Http302, ExceptionResponseView
from django_powerbank.views.auth import AuthenticatedView, StaffRequiredMixin
from django_powerbank.views.mixins import ReturnUrlMx
from pascal_templates import CreateView, DeleteView, DetailView, ListView, UpdateView

from . import forms, models, tasks

