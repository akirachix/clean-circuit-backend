from django.contrib import admin
from .models import Upcycler, UpcyclerClothesRequest,UpcycledProduct

# Register your models here.
admin.site.register(Upcycler)
admin.site.register(UpcyclerClothesRequest)
admin.site.register(UpcycledProduct)
