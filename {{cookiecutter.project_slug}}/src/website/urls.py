
"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView
from django.views.generic import TemplateView, RedirectView
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import JavaScriptCatalog

from introduce.forms import RevalidationPasswordResetForm
from misc.views import ErrorView

from . import debug

sitemaps = {}

if not settings.DEBUG:
    handler500 = ErrorView.as_view(template_name="errors/500.html")

handler400 = ErrorView.as_view(template_name="errors/400.html", status_code=400)
handler403 = ErrorView.as_view(template_name="errors/403.html", status_code=403)

from . import api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^err/', debug.ErrView.as_view(), name='err'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^i18n/', include('misc.choose_language.urls')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^accounts/password_reset/$', PasswordResetView.as_view(form_class=RevalidationPasswordResetForm), name='password_reset'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/registration/register/', RedirectView.as_view(pattern_name='introduce:register_user'), name='registration_register'),  # hide defatult view,
    url(r'^accounts/registration/', include('registration.backends.hmac.urls')),
    url(r'^accounts/social/', include('social_django.urls', namespace='social')),
    url(r'^accounts/social/login-error$', TemplateView.as_view(template_name='errors/social_login_error.html')),
    url(r'^help/', RedirectView.as_view(url='http://help.your.hr'), name='website-help'),
    url(r'^', include('{{ cookiecutter.app_name }}.urls')),
    url(r'^legal/privacy$', TemplateView.as_view(template_name="legal/privacy.html"), name="privacy"),
    url(r'^legal/tos$', TemplateView.as_view(template_name="legal/tos.html"), name="tos"),
    url(r'^demo$', TemplateView.as_view(template_name="common/demo.html"), name="demo"),
    url(r'^status$', TemplateView.as_view(template_name="common/status.html"), name="status"),
    url(r'^api/', include(api.router.urls)),
]

if settings.DEBUG or 'SHOW_TOOLBAR_CALLBACK' in settings.DEBUG_TOOLBAR_CONFIG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
