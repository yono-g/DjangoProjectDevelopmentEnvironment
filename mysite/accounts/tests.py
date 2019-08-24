from django.test import TestCase
from mysite.accounts.models import User


class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test',
            'password': 'test',
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
