from rest_framework import serializers
from login.models import Person, Company, Role

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
                    'company_prn')

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


