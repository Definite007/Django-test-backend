from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=80)
    DepartmentName = models.CharField(max_length=40)
    DateOfJoining = models.DateField()
    
    def __str__(self):
        return (self.EmployeeName)