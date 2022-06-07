from rest_framework import serializers
from home.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId',
                'EmployeeName',
                'DepartmentName',
                'DateOfJoining'
                )