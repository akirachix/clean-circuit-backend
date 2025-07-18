from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('trader', 'Trader'),
        ('upcycler', 'Upcycler'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='upcycler')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class UpcyclerClothesRequest(models.Model):
    request = models.AutoField(primary_key=True)
    upcycler = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='upcycler_images/', null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='clothes_request_images/', null=True, blank=True)
    def __str__(self):
        return f"{self.type} request by {self.upcycler.name}"