from django.contrib import admin

# Register your models here.

from .models import User, Material
# Register your models here.
# admin.site.register(User)  # Removed or comment out since User is not defined
admin.site.register(Material)
admin.site.register(User)