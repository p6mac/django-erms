from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from home.models import Employees, EmployeesForm
from departments.models import Departments
from django.views.generic import TemplateView
# Create your views here.
class ManageEmployeesView :
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


class HomeView(TemplateView) :
    template_name = 'manage_employees.html'
    
    def get_context_data(self, request) :
        context = {
            'account_name' : request.session.get('username'),
            'employees' : Employees.objects.select_related('department').all(),
            'departments' : Departments.objects.all()
        }
        return context

    def get(self, request, status=None, **kwargs) :
        view_data = self.get_context_data(request)
        if request.session.get('is_login') is None:
                return HttpResponseRedirect('/')
        
        if status is not None :
            view_data['status'] = status
            
        return render(request, self.template_name, view_data)
    
    def post(self, request) :
        view_data = self.get_context_data(request)

        form = EmployeesForm(request.POST)
        if form.is_valid() :
            new_employee = form.save()
            is_new_employee_save = Employees.objects.filter(id = new_employee.id).exists()
            if is_new_employee_save :
                status = 'success'
            else :
                status = 'error'
        
        return redirect('/manage_employees/%s' % status)


# class EditEmployeeView(TemplateView) :
#     template_name = 'edit_employees.html'

#     def get(self, request, user_id) :
        

