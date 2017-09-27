from datetime import datetime
from functools import reduce
from urllib.parse import urlencode

import logging
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import resolve_url
from django.utils import timezone
from django.utils.formats import localize
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django_ad_sync.models import AdInfo
from django_powerbank.db.models.base import BaseModel
from django_powerbank.db.models.fields import BinaryMaskEnum, ChoicesIntEnum, MarkDownField

