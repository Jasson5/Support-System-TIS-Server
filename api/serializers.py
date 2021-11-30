from rest_framework import serializers
from api.models import Announcement, Attendance, Calendar, Homework, Offer, Person, Company, Role, Semester

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (  'personId',
                    'name',
                    'surname1',
                    'surname2',
                    'personEmail',
                    'password',
                    'role_prn',
                    'company_prn',
                    'semester_prn')

class  CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (  'shortName',
                    'longName',
                    'society',
                    'address',
                    'telephone',
                    'companyEmail',
                    'statusCompany',
                    'homework')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (  'roleId',
                    'roleName')

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = (  'semesterId',
                    'semesterName',
                    'semesterPassword')

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (  'announcementId',
                    'dateAnn',
                    'description',
                    'file')

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = (  'offerId',
                    'dateOffer',
                    'descriptionOffer',
                    'fileOffer',
                    'minOffer',
                    'maxOffer')    

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = (  'homeworkId',
                    'tittleHw',
                    'descriptionHw',
                    'dateDeliveryHw',
                    'datePublicationHw',
                    'statusHw',
                    'fileHw',
                    'gradeHw')  

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = (  'calendarId',
                    'descriptionCalendar',
                    'observationCalendar',
                    'dateCalendar',
                    'company_calendar'
                    )    

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = (  'attendanceId',
                    'dateAttendance',
                    'noteAttendance',
                    'statusAttendance',
                    'gradeAttendance',
                    'gradePOV',
                    'person_attendance'
                    ) 

   
