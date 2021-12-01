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
   class Meta:
       verbose_name='semester'
       verbose_name_plural='semesters'

class Announcement(models.Model):
   announcementId=models.AutoField(primary_key=True)
   dateAnn=models.DateTimeField(auto_now_add=True)
   description=models.CharField(max_length=500)
   file=models.CharField(max_length=2000)
   def __str__(self):
       return self.description
   class Meta:
       verbose_name='announcement'
       verbose_name_plural='announcement'

class Offer(models.Model):
   offerId=models.AutoField(primary_key=True)
   dateOffer=models.DateTimeField(auto_now_add=True)
   descriptionOffer=models.CharField(max_length=500)
   fileOffer=models.CharField(max_length=2000)
   minOffer=models.IntegerField()
   maxOffer=models.IntegerField()
   def __str__(self):
       return self.descriptionOffer
   class Meta:
       verbose_name='offer'
       verbose_name_plural='offers'

class Homework(models.Model):
    homeworkId=models.AutoField(primary_key=True)
    tittleHw=models.CharField(max_length=50)
    descriptionHw=models.CharField(max_length=300)
    dateDeliveryHw=models.DateTimeField()
    datePublicationHw=models.DateTimeField(auto_now_add=True)
    statusHw=models.BooleanField(auto_created=False)
    fileHw=models.CharField(max_length=2000)
    gradeHw=models.CharField(max_length=50) 
    def __str__(self):
       return self.tittleHw
    class Meta:
       verbose_name='homework'
       verbose_name_plural='homeworks'
   
class Company(models.Model):
    companyId=models.AutoField(primary_key=True)
    shortName=models.CharField(max_length=50, unique=True)
    longName=models.CharField(max_length=50)
    society=models.CharField(max_length=5)
    address=models.CharField(max_length=100)
    telephone=models.IntegerField()
    companyEmail =models.EmailField(max_length=50)
    statusCompany=models.BooleanField(default=False)
    homework= models.ManyToManyField(Homework, blank=True)
    def __str__(self):
        return self.shortName
    class Meta:
       verbose_name='Company'
       verbose_name_plural='Companies'

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

class Calendar(models.Model):
   calendarId=models.AutoField(primary_key=True)
   descriptionCalendar=models.CharField(max_length=300)
   observationCalendar=models.CharField(max_length=500)
   dateCalendar=models.DateField(auto_now_add=True)
   company_calendar=models.ForeignKey(Company, null=False, blank=False , on_delete=models.CASCADE) 
   def __str__(self):
       return self.dateCalendar
   class Meta:
       verbose_name='calendar'
       verbose_name_plural='calendars'

class Attendance(models.Model):
   attendanceId=models.AutoField(primary_key=True)
   dateAttendance=models.DateField()
   noteAttendance=models.CharField(max_length=500)
   statusAttendance=models.IntegerField()
   gradeAttendance=models.IntegerField()
   gradePOV=models.IntegerField()
   person_attendance=models.ForeignKey(Person, null=False, blank=False , on_delete=models.CASCADE)
   def __str__(self):
       return self.statusAttendance
   class Meta:
       verbose_name='attendance'
       verbose_name_plural='attendances'



