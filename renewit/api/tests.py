
from django.test import TestCase
from Material.models import Material
from django.utils import timezone

class MaterialModelTest(TestCase):
    def test_create_material(self):
        material = Material.objects.create(
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
       











    
=======
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MaterialCatalogue

class MaterialCatalogueViewSetTests(APITestCase):
    def setUp(self):
        # Create a sample material for testing
        self.material = MaterialCatalogue.objects.create(material_type='Fabric', other_field='Sample Data')

    def test_create_material(self):
        url = reverse('materialcatalogue-list')  # Adjust the URL name as per your routing
        data = {
            'material_type': 'New Fabric',
            'other_field': 'New Sample Data'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MaterialCatalogue.objects.count(), 2)  # Check if a new material is created
        self.assertEqual(MaterialCatalogue.objects.get(id=response.data['id']).material_type, 'New Fabric')

    def test_update_material(self):
        url = reverse('materialcatalogue-list')  # Adjust the URL name as per your routing
        data = {
            'material_type': 'Fabric',  # This should match the existing material_type
            'other_field': 'Updated Sample Data'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.material.refresh_from_db()
        self.assertEqual(self.material.other_field, 'Updated Sample Data')

    def test_invalid_material_creation(self):
        url = reverse('materialcatalogue-list')
        data = {
            'material_type': '',  # Invalid data
            'other_field': 'Sample Data'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_or_create_material(self):
        url = reverse('materialcatalogue-list')  # Adjust the URL name as per your routing
        data = {
            'material_type': 'Fabric',  # This should match the existing material_type
            'other_field': 'Another Sample Data'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MaterialCatalogue.objects.count(), 1)  # Ensure no new material is created
        self.assertEqual(self.material.other_field, 'Another Sample Data')  # Check if the existing material is updated

>>>>>>> d9462d9ed5966ecebc715070f6c4099dcd90189b
