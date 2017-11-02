from django.shortcuts import render
from departments.models import Departments, DepartmentsForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
class DepartmentsView(TemplateView) :
    template_name = 'manage_departments.html'
    def get(self, request) :
        context = {
            'departments' : Departments.objects.all(),
            'account_name' : request.session.get('username')
        }
        return render(request, self.template_name, context)

    def post(self, request) :
        form = DepartmentsForm(request.POST)

        if form.is_valid() :
            form.save()

        return redirect('/manage_departments')

class ManageDepartment :
    
    def edit(self, request, id) :
        pass


    def delete(self, request, id) :
        pass
        
