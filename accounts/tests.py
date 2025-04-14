from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="xerx", email="xerx@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "xerx")
        self.assertEqual(user.email, "xerx@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(
            username="super", email="super@email.com", password="testpass123"
        )
        self.assertEqual(admin.username, "super")
        self.assertEqual(admin.email, "super@email.com")
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
