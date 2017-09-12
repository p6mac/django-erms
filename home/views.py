from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from home.models import Employees, EmployeesForm

# Create your views here.
class ManageEmployeesView :
    @csrf_exempt
    def index(self, request) : 
        data = Employees.objects.all()
        view_data = {
            'employees' : data,
            'account_name' : request.session.get('username'),
        }
        if request.method == 'POST' :
            form = EmployeesForm(request.POST)
            if form.is_valid() :
                new_employee = form.save()
                is_new_employee_save = Employees.objects.filter(id = new_employee.id).exists()
                if is_new_employee_save :
                    view_data['is_save'] = True
                else :
                    view_data['is_error'] = True
        return render(request, 'manage_employees.html', view_data)

    @csrf_exempt
    def edit(self, request, id) :
        view_data = {}
        if id :
            view_data['account_name'] = request.session.get('username')
            if request.method == 'GET' :
                view_data['employee_info'] = Employees.objects.get(id = id)

            elif request.method == 'POST' :
                POST = request.POST

                form = EmployeesForm(POST)
                if form.is_valid() :
                    is_update = Employees.update(id, POST)
                    if is_update :
                        view_data['is_update'] = True
                        view_data['employee_info'] = Employees.objects.get(id = id)
                    else:
                        view_data['is_error'] = True
                        
                
            return render(request, 'edit_employees.html', view_data)
        else :
            return HttpResponseRedirect('/manage_employees')


    def delete(self, request, id) :
        response_data = {
            'is_deleted' : False
        }
        if id :
            Employees.objects.filter(id = id).delete()
            if Employees.objects.filter(id = id).exists() == False :
                response_data['is_deleted'] = True
                return redirect('/manage_employees', id = id)
        else :
            return redirect('/manage_employees')

