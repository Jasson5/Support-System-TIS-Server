from django.contrib import admin
from .models import Announcement, Company, Role, Person, Semester, Offer
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Company)
admin.site.register(Semester)
admin.site.register(Announcement)
admin.site.register(Offer)

TokenAdmin.raw_id_fields = ['user']