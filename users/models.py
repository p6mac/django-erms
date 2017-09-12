from django.db import models, connection
from login.models import User
# Create your models here.
class Users(models.Model) :
    account_id = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'

    def get_all() :
            query = """SELECT * 
                       FROM accounts 
                       LEFT JOIN users 
                       ON accounts.id = users.account_id"""
            results = User.objects.raw(query)
            return results