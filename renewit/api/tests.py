from django.test import TestCase
from user_role.models import User
from user_role.models import Material

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

from django.utils import timezone

class MaterialModelTest(TestCase):
    def setUp(self):
        self.trader = User.objects.create(
            name='Trader User',
            email='traderuser@example.com',
            phone='0987654321',
            role='trader',
        )

    def test_create_material(self):
        material = Material.objects.create(
            trader=self.trader,
            type='cotton',
            quantity=7,
            image='null',  
            condition='high',
            listed_at=timezone.now()  
        )
        self.assertEqual(Material.objects.count(), 1)
        self.assertEqual(material.type, 'cotton')
        self.assertEqual(material.quantity, 7)
        self.assertEqual(material.condition, 'high')
        self.assertEqual(material.trader, self.trader)











    