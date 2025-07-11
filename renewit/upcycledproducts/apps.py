from django.apps import AppConfig



class UpcycledproductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upcycledproducts'


class MaterialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Material'

class UserRoleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_role'


