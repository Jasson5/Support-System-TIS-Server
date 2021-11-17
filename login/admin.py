from django.contrib import admin
from .models import Company, Role, Person
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Company)

TokenAdmin.raw_id_fields = ['user']