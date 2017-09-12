from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users
# Create your views here.
class UsersView :
    def index(self, request) :
        view_data = {
            'users' : Users.get_all(),
            'account_name' : request.session.get('username'),
        }
        return render(request, 'manage_users.html', view_data)
        
