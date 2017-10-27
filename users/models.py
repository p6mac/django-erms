from django.db import models, connection
from login.models import User
# Create your models here.
class Users() :
    def get_all() :
            query = """SELECT * 
                       FROM accounts 
                       LEFT JOIN users 
                       ON accounts.id = users.account_id"""
            results = User.objects.raw(query)
            return results