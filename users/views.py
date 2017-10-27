from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from users.models import Users
from login.models import Account, User
from django.core.serializers import serialize
# Create your views here.
class UsersView :
    def index(self, request) :
        view_data = {
            'users' : User.objects.select_related('account').all(),
            'account_name' : request.session.get('username'),
        }
        if request.method == 'GET' :
            if request.session.get('is_login') is None:
                return HttpResponseRedirect('/')

        return render(request, 'manage_users.html', view_data)

    def delete(self, request, id) :
        Account.objects.filter(pk = id).delete()
        return HttpResponseRedirect('/manage_users')
