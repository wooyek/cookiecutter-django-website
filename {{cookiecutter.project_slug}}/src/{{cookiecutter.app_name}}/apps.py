from django.apps import AppConfig
from django.utils.translation import ugettext as __, ugettext_lazy as _


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = '{{ cookiecutter.app_name }}'
    verbose_name = _('{{ cookiecutter.app_name }}')
