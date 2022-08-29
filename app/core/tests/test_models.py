"""
    Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    """Test User Models. """

    def test_create_user_with_email_successfull(self):
        """ Test create user with email """
        email = "testemail@mail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """" Test email is normalized for new user """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'passpass123')

    def test_create_superuser(self):
        """ Test Super user create """
        user = get_user_model().objects.create_superuser(
            email='user@email.com',
            password='testpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
