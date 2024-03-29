from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Person, Company, Role, Semester, Announcement, Offer, Homework, Attendance, Calendar
from api.serializers import PersonSerializer, CompanySerializer, RoleSerializer, SemesterSerializer, AnnouncementSerializer, OfferSerializer, HomeworkSerializer, AttendanceSerializer, CalendarSerializer

'''def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            messages.success(request, f'Usario {username} creado')
    else:
        form = UserCreationForm()
    context={'form' : form}
    return render(request, "registro.html", context)'''
# Create your views here.

@csrf_exempt
def PersonApi(request, id=0):
    if request.method=='GET':
        person = Person.objects.all()
        person_serializer = PersonSerializer(person, many=True)
        return  JsonResponse(person_serializer.data, safe=False)

    elif request.method=='POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        person_data = JSONParser().parse(request)
        person = Person.objects.get(personId=person_data['personId'] )
        person_serializer = PersonSerializer(person, data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        person = Person.objects.get(personId=id)
        person.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


@csrf_exempt
def CompanyApi(request, id=0):
    if request.method=='GET':
        company = Company.objects.all()
        company_serializer = CompanySerializer(company, many=True)
        return  JsonResponse(company_serializer.data, safe=False)

    elif request.method=='POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(companyId=company_data['companyId'] )
        company_serializer = CompanySerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        company = Company.objects.get(companyId=id)
        company.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


@csrf_exempt
def RoleApi(request, id=0):
    if request.method=='GET':
        role = Role.objects.all()
        role_serializer = RoleSerializer(role, many=True)
        return  JsonResponse(role_serializer.data, safe=False)
        
    elif request.method=='POST':
        role_data = JSONParser().parse(request)
        role_serializer = RoleSerializer(data=role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        role_data = JSONParser().parse(request)
        role = Role.objects.get(roleId=role_data['roleId'] )
        role_serializer = RoleSerializer(role, data=role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        role = Role.objects.get(roleId=id)
        role.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


@csrf_exempt
def SemesterApi(request, id=0):
    if request.method=='GET':
        semester = Semester.objects.all()
        semester_serializer = SemesterSerializer(semester, many=True)
        return  JsonResponse(semester_serializer.data, safe=False)
        
    elif request.method=='POST':
        semester_data = JSONParser().parse(request)
        semester_serializer = SemesterSerializer(data=semester_data)
        if semester_serializer.is_valid():
            semester_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        semester_data = JSONParser().parse(request)
        semester = Semester.objects.get(semesterId=semester_data['semesterId'] )
        semester_serializer = SemesterSerializer(semester, data=semester_data)
        if semester_serializer.is_valid():
            semester_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        semester = Semester.objects.get(semesterId=id)
        semester.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)

@csrf_exempt
def AnnouncementApi(request, id=0):
    if request.method=='GET':
        announcement = Announcement.objects.all()
        announcement_serializer = AnnouncementSerializer(announcement, many=True)
        return  JsonResponse(announcement_serializer.data, safe=False)
        
    elif request.method=='POST':
        announcement_data = JSONParser().parse(request)
        announcement_serializer = AnnouncementSerializer(data=announcement_data)
        if announcement_serializer.is_valid():
            announcement_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        announcement_data = JSONParser().parse(request)
        announcement = Announcement.objects.get(announcementId=announcement_data['announcementId'] )
        announcement_serializer = AnnouncementSerializer(announcement, data=announcement_data)
        if announcement_serializer.is_valid():
            announcement_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        announcement = Announcement.objects.get(announcementId=id)
        announcement.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)

@csrf_exempt
def OfferApi(request, id=0):
    if request.method=='GET':
        offer = Offer.objects.all()
        offer_serializer = OfferSerializer(offer, many=True)
        return  JsonResponse(offer_serializer.data, safe=False)
        
    elif request.method=='POST':
        offer_data = JSONParser().parse(request)
        offer_serializer = OfferSerializer(data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        offer_data = JSONParser().parse(request)
        offer = Offer.objects.get(offerId=offer_data['offerId'] )
        offer_serializer = OfferSerializer(offer, data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        offer = Offer.objects.get(offerId=id)
        offer.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)

@csrf_exempt
def HomeworkApi(request, id=0):
    if request.method=='GET':
        homework = Homework.objects.all()
        homework_serializer = HomeworkSerializer(homework, many=True)
        return  JsonResponse(homework_serializer.data, safe=False)
        
    elif request.method=='POST':
        homework_data = JSONParser().parse(request)
        homework_serializer = HomeworkSerializer(data=homework_data)
        if homework_serializer.is_valid():
            homework_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        homework_data = JSONParser().parse(request)
        homework = Homework.objects.get(homeworkId=homework_data['homeworkId'] )
        homework_serializer = HomeworkSerializer(homework, data=homework_data)
        if homework_serializer.is_valid():
            homework_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        homework = Homework.objects.get(homeworkId=id)
        homework.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)

@csrf_exempt
def CalendarApi(request, id=0):
    if request.method=='GET':
        calendar = Calendar.objects.all()
        calendar_serializer = CalendarSerializer(calendar, many=True)
        return  JsonResponse(calendar_serializer.data, safe=False)
        
    elif request.method=='POST':
        calendar_data = JSONParser().parse(request)
        calendar_serializer = CalendarSerializer(data=calendar_data)
        if calendar_serializer.is_valid():
            calendar_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        calendar_data = JSONParser().parse(request)
        calendar = Calendar.objects.get(calendarId=calendar_data['calendarId'] )
        calendar_serializer = CalendarSerializer(calendar, data=calendar_data)
        if calendar_serializer.is_valid():
            calendar_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        calendar = Calendar.objects.get(calendarId=id)
        calendar.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)

@csrf_exempt
def AttendanceApi(request, id=0):
    if request.method=='GET':
        attendance = Attendance.objects.all()
        attendance_serializer = AttendanceSerializer(attendance, many=True)
        return  JsonResponse(attendance_serializer.data, safe=False)
        
    elif request.method=='POST':
        attendance_data = JSONParser().parse(request)
        attendance_serializer = AttendanceSerializer(data=attendance_data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        attendance_data = JSONParser().parse(request)
        attendance = Attendance.objects.get(attendanceId=attendance_data['attendanceId'] )
        attendance_serializer = AttendanceSerializer(attendance, data=attendance_data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        attendance = Attendance.objects.get(attendanceId=id)
        attendance.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)
   

class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user.email),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.pk,
            'email': user.email
        })

    """from rest_framework_simplejwt.views import TokenObtainPairView

    class Login(TokenObtainPairVIew):
        serializer_class = CustomTokenObtainPairSerializer"""