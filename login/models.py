from django.db import models
from django.forms import ModelForm

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'accounts'



        
    
class AccountForm(ModelForm) :
    class Meta :
        model = Account
        fields = '__all__'
    

class User(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE, default='')
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField(default='')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'users'
