"""
    Tests for the User API.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


CREATE_USER_URL = reverse('users:create')


def create_user(**params):
    """ Create User. """
    return get_user_model().objects.create(**params)


class PublicUserApiTest(TestCase):
    """ Test the public feature of the user api. """
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_user_successfull(self):
        """ Test succession of creating new user. """
        payload = {
            'email': 'test@email.com',
            'password': 'testpass123',
            'name': 'Test User',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_create_with_email_exists(self):
        """ Test Create user with existed email. """
        payload = {
            'email': 'test@email.com',
            'password': 'testklasd123',
            'name': 'Test koko',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_short_password(self):
        """ Test Create User with short password. """
        payload = {
            'email': 'test@email.com',
            'password': 'pwd',
            'name': 'Testawy',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)
