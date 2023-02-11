from django.contrib import admin
from Store.models import Departments, Employees
# Register your models here.


class Department(admin.ModelAdmin):
    list_display = ('IdDepartment','DepartmentName')

    list_display_links = ('DepartmentName',)

    search_fields = ('IdDepartment', 'DepartmentName')

    list_per_page = 20

# Passo (Model, classe-no-admin)
admin.site.register(Departments, Department)

class Employee(admin.ModelAdmin):
    list_display = ('IdEmployee','EmployeeName','Department', 'DateOfJoining')

    list_display_links = ('EmployeeName', 'DateOfJoining')

    search_fields = ('IdEmployee','EmployeeName','Department', 'DateOfJoining')

    list_per_page = 20

# Passo (Model, classe-no-admin)
admin.site.register(Employees, Employee)
