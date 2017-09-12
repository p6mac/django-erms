from django.db import models
from django.forms import ModelForm

import datetime
# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'accounts'
    
class AccountForm(ModelForm) :
    class Meta :
        model = Account
        fields = '__all__'
    

class User(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        manage : False
        db_table = 'users'
