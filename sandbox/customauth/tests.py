import re
from django.core import mail
from django.urls import reverse
from django.test import TestCase

from sandbox.customauth.models import User


class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'password': 'test',
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post(reverse('customauth:login'), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        response = self.client.get(reverse('customauth:logout'), follow=True)
        self.assertFalse(response.context['user'].is_authenticated)


class ResetPasswordTest(TestCase):

    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'password': 'test',
        }
        User.objects.create_user(**self.credentials)

    def test_password_reset(self):
        self.client.post(reverse('customauth:password_reset'), {
            'email': self.credentials['email']
        }, follow=True)

        self.assertEqual(len(mail.outbox), 1)

        matchOB = re.search(r'http://testserver(.+)', mail.outbox[0].body)
        confirm_page_path = matchOB.groups()[0]
        response = self.client.get(confirm_page_path, follow=True)
        redirected_path = response.request['PATH_INFO']
        new_password = '6"Mp6s/J'
        response = self.client.post(redirected_path, {
            'new_password1': new_password,
            'new_password2': new_password,
        }, follow=True)

        response = self.client.post(reverse('customauth:login'), {
            'email': self.credentials['email'],
            'password': new_password
        }, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
