from rest_framework import serializers
from login.models import Person, Company, Role, Semester

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
        fields = (  'companyId',
                    'shortName',
                    'longName',
                    'society',
                    'address',
                    'telephone',
                    'companyEmail')

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
        model = Semester
        fields = (  'announcementId',
                    'person_ann',
                    'date_ann',
                    'description',
                    'file')

class PseeAnnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = (  'prn_pseeann',
                    'ann_pseeann',
                    )                    
