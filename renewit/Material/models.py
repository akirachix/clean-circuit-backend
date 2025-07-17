from django.db import models
from django.contrib.auth.models import User
from user_role.models import User

class Material(models.Model):
    material = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    trader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materials')
    image = models.ImageField(upload_to='material_images/', null=True, blank=True)
    condition = models.CharField(max_length=50)
    listed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type