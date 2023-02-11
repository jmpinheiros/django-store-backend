from django.db import models

# Create your models here.
class Departments(models.Model):
    IdDepartment = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employees(models.Model):
    IdEmployee = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
