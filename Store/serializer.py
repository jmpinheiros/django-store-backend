from Store.models import Employees, Departments
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('IdDepartment', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('IdEmployee',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
