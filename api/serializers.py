from rest_framework import serializers
from .models import Company, Employee

# Create Serializer Here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField() #for showing company_id which is not showing defaultly
    class Meta:
        model = Company
        fields = "__all__"
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() #for showing id which is not showing defaultly
    class Meta:
        model = Employee
        fields = "__all__"