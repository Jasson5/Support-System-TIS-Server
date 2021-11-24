from rest_framework import serializers
from api.models import Announcement, Offer, Person, Company, Role, Semester

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
        model = Announcement
        fields = (  'announcementId',
                    'dateAnn',
                    'description',
                    'file')

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = (  'OfferId',
                    'dateOffer',
                    'descriptionOffer',
                    'fileOffer',
                    'minOffer',
                    'maxOffer')       
