from datetime import datetime
from functools import reduce

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q
from django.forms import model_to_dict
from django.utils import timezone
from django.utils.formats import localize
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django_ad_sync.models import AdInfo
from django_powerbank.db.models.base import BaseModel


class Example(models.Model):
    user = models.ForeignKey(get_user_model())
