from django.shortcuts import render
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.contrib.auth import authenticate, login , logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from login.models import Account, AccountForm, User
from bcrypt import hashpw, checkpw
# Create your views here.
class LoginView :
    @csrf_exempt
    def index(self, request) :
        isInvalidCredentials = False

        if request.method == 'GET' :
            if request.session.get('is_login') is not None:
                return HttpResponseRedirect('/manage_employees')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try :
                user = Account.objects.filter(username = username).get()
                print(check_password(password, user.password))
                print(user.password)
                print(password.encode('UTF_8'))
                print(make_password(password.encode('UTF_8')))
                if password == user.password :
                    request.session['account_id'] = user.id,
                    request.session['username'] = user.username
                    request.session['is_login'] = True
                    return HttpResponseRedirect('/manage_employees')
                else:
                    isInvalidCredentials = True
            except Account.DoesNotExist :
                isInvalidCredentials = True
                
        return render(request, 'login_form.html', {'error' : isInvalidCredentials })
    @csrf_exempt
    def register(self, request):
        view_data = {}
        if request.method == 'POST' :
            POST = request.POST
            form = AccountForm(POST)
            if form.is_valid() :
                if not Account.objects.filter(username = POST['username']).exists() :
                    save_account = form.save()
                    # save_account.password = make_password(POST['password'])
                    # save_account.save()
                    if save_account.pk :
                        new_user = User.objects.create(account_id = save_account.pk, first_name = POST['first_name'], last_name = POST['last_name'])
                        new_user.save()
                        if new_user.pk :
                            view_data['new_create'] = True
                        else:
                            view_data['err_new_create'] = True
                    else :  
                        view_data['err_new_create'] = True
                else :  
                    view_data['err_new_create'] = True
            else :
                view_data['err_new_create'] = True                                      
            
        return render(request, 'register_form.html', view_data)
        

    def logout(self, request) :
        try :
            request.session.clear()
        except KeyError :
            pass
        return HttpResponseRedirect('/')
        
            