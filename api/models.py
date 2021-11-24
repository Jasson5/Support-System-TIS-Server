from django.db import models
from django.db.models.base import Model
import random
import string
from django.db.models.deletion import CASCADE

from django.urls.resolvers import CheckURLMixin
from rest_framework.fields import CharField
# Create your models here.
def generarPassword(n):
   s=""
   caracteres= list(string.printable)
   caracteres=caracteres[:-40]
   for i in range(n):
      s+=random.choice(caracteres)
   return s
   
    
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

class Semester(models.Model):
   semesterId= models.AutoField(primary_key=True)
   semesterName= models.CharField(max_length=7)
   semesterPassword=models.CharField(default=generarPassword(15), max_length=20)
   def __str__(self):
       return self.semesterName

class Announcement(models.Model):
   announcementId=models.AutoField(primary_key=True)
   dateAnn=models.DateTimeField(auto_now_add=True)
   description=models.CharField(max_length=500)
   file=models.FileField(upload_to = "Uploaded Files/")

class Offer(models.Model):
   offerId=models.AutoField(primary_key=True)
   dateOffer=models.DateTimeField(auto_now_add=True)
   descriptionOffer=models.CharField(max_length=500)
   fileOffer=models.FileField(upload_to = "Uploaded Files/")
   minOffer=models.IntegerField()
   maxOffer=models.IntegerField()

class Person(models.Model):
    personId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    surname1=models.CharField(max_length=50)
    surname2=models.CharField(max_length=50)
    personEmail=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    role_prn=models.ForeignKey(Role,null=False, blank=False , on_delete=models.CASCADE) 
    company_prn=models.ForeignKey(Company,null=True, blank=True, on_delete=models.CASCADE) #no tiene grupo=0
    semester_prn=models.ForeignKey(Semester, null=False, blank=False, on_delete=models.CASCADE)
    announcements= models.ManyToManyField(Announcement, blank=True)
    offers= models.ManyToManyField(Offer, blank=True)
    def __str__(self):
       return self.name
    class Meta:
       verbose_name='person'
       verbose_name_plural='persons'


