from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='app_user_profile')
    ROLE_CHOICES = [
        ('trader', 'Trader'),
        ('upcycler', 'Upcycler'),
    ]
    name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)

    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='upcycler')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UpcyclerClothesRequest(models.Model):
    request = models.AutoField(primary_key=True)
    upcycler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clothes_requests')
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='clothes_request_images/', null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} request by {self.upcycler.name}"
