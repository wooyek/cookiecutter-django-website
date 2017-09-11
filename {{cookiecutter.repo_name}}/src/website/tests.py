# coding=utf-8
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from django.test import TestCase
from django_powerbank.testing import MigrationsCheck


class MigrationsCheckTests(MigrationsCheck):
    pass


class TestAdminAvailable(TestCase):
    def setUp(self):
        self.user = get_user_model()(email="foo@bar.com", is_superuser=False, is_staff=True, is_active=True)
        self.user.save()
        self.client.force_login(self.user, settings.AUTHENTICATION_BACKENDS[0])

    def test_admin_get(self):
        url = resolve_url("admin:index")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
