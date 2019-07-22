from django.test import TestCase
from mysite.accounts.models import User


class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'password': 'test',
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        response = self.client.get('/logout/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
