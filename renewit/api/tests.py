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
       











    