from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    USER = 'admin'
    PASSWORD = '1234qwer'
    EMAIL = 'test@test.com'

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.user = get_user_model().objects.create_user(username=self.USER, password=self.PASSWORD, email=self.EMAIL)
        token = Token.objects.get(user__username=self.USER)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
