from django.shortcuts import render
from departments.models import Departments
from django.views.generic import TemplateView

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
        print(request.POST)