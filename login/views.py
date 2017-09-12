from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from login.models import Account, AccountForm, User

# Create your views here.
class LoginView :
    @csrf_exempt
    def index(self, request) :
        isInvalidCredentials = False
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            check_user = Account.objects.filter(username = username, password = password).exists()
            if check_user :
                user = Account.objects.filter(username = username, password = password).get()
                request.session['account_id'] = user.id,
                request.session['username'] = user.username
                request.session['is_login'] = True
                return HttpResponseRedirect('/manage_employees')
            else:
                isInvalidCredentials = True;
        return render(request, 'login_form.html', {'error' : isInvalidCredentials })
    @csrf_exempt
    def register(self, request):
        view_data = {}
        if request.method == 'POST' :
            POST = request.POST
            form = AccountForm(POST)
            if form.is_valid() :
                save_account = form.save()
                if save_account.id :
                    new_user = User.objects.create(account_id = save_account.id, first_name = POST['first_name'], last_name = POST['last_name'])
                    new_user.save()
                    if new_user.pk :
                        view_data['new_create'] = True
                    else:
                        view_data['err_new_create'] = True
                else :  
                    view_data['err_new_create'] = True
            else :
                view_data['err_new_create'] = True                                      
            
        return render(request, 'register_form.html', view_data)
        

    def logout(self, request) :
            del request.session['username']
            del request.session['is_login']
            return HttpResponseRedirect('/')
        
            