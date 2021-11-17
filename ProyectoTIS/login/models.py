from django.db import models
from django.db.models.base import Model

# Create your models here.

    
class Company(models.Model):
    companyId=models.AutoField(primary_key=True)
    shortName=models.CharField(max_length=50)
    longName=models.CharField(max_length=50)
    society=models.CharField(max_length=5)
    address=models.CharField(max_length=100)
    telephone=models.IntegerField()
    companyEmail =models.EmailField(max_length=50)
    def __str__(self):
        return self.shortName
    class Meta:
       verbose_name='Company'
       verbose_name_plural='Companies'


class Role(models.Model):
    roleId=models.AutoField(primary_key=True)
    roleName=models.CharField(max_length=50)
    def __str__(self):
       return self.roleName
    class Meta:
       verbose_name='role'
       verbose_name_plural='roles'


class Person(models.Model):
    personId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    surname1=models.CharField(max_length=50)
    surname2=models.CharField(max_length=50)
    personEmail=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    role_prn=models.ForeignKey(Role,null=False, blank=False , on_delete=models.CASCADE) 
    company_prn=models.ForeignKey(Company,null=False, blank=False, on_delete=models.CASCADE) #no tiene grupo=0
    def __str__(self):
       return self.name
    class Meta:
       verbose_name='person'
       verbose_name_plural='persons'