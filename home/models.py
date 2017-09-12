from django.db import models
from django.forms import ModelForm
# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=121)
    salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employees'

    def update(id, *post_data) :
         if Employees.objects.filter(pk = id).exists() :
            employee = Employees.objects.get(pk = id)
            employee.first_name = post_data['first_name']
            employee.last_name = post_data['last_name']
            employee.birthdate = post_data['birthdate']
            employee.address = post_data['address']
            employee.age = post_data['age']
            employee.salary = post_data['salary']
            is_save = employee.save()
            if Employees.objects.filter(pk = id).exists() :
                return True
            else :
                return False


        


class EmployeesForm(ModelForm) :
    class Meta :
        model = Employees
        fields = '__all__'
        