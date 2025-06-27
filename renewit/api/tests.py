from django.test import TestCase
from user_role.models import User, UpcyclerClothesRequest

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='testuser@example.com',
            phone='1234567890',
            role='trader',
        )

    def test_create_user(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.name, 'Test User')

    def test_read_user(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.email, 'testuser@example.com')

    def test_update_user(self):
        self.user.name = 'Updated Name'
        self.user.save()
        updated_user = User.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.name, 'Updated Name')

    def test_delete_user(self):
        self.user.delete()
        self.assertEqual(User.objects.count(), 0)

class UpcyclerClothesRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Upcycler User',
            email='mary@gmail.com',
            phone='0787654321',
            role='upcycler',
        )
        self.request = UpcyclerClothesRequest.objects.create(
            upcycler=self.user,
            type='Shirt',
            quantity=10,
        )

    def test_create_clothes_request(self):
        self.assertEqual(UpcyclerClothesRequest.objects.count(), 1)
        self.assertEqual(self.request.type, 'Shirt')

    def test_read_clothes_request(self):
        req = UpcyclerClothesRequest.objects.get(pk=self.request.pk)
        self.assertEqual(req.quantity, 10)

    def test_update_clothes_request(self):
        self.request.type = 'Pants'
        self.request.quantity = 5
        self.request.save()
        updated = UpcyclerClothesRequest.objects.get(pk=self.request.pk)
        self.assertEqual(updated.type, 'Pants')
        self.assertEqual(updated.quantity, 5)

    def test_delete_clothes_request(self):
        self.request.delete()
        self.assertEqual(UpcyclerClothesRequest.objects.count(), 0)