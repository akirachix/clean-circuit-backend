from django.test import TestCase
from user_role.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            name='Test User',
            email='testuser@example.com',
            phone='1234567890',
            role='trader',
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.role, 'trader')