from django.db import models

# Create your models here.
class Departments(models.Model) :
    department_name = models.TextField()
    department_head = models.TextField()
    department_desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'departments'
