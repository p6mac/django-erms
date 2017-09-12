from django.conf.urls import url
from home.views import ManageEmployeesView

urlpatterns = [
    url(r'^manage_employees', ManageEmployeesView().index, name = 'manage_employees'),
    url(r'^manage_employee/edit/(?P<id>\d+)/$', ManageEmployeesView().edit, name="edit_employee"),
    url(r'^manage_employee/delete/(?P<id>\d+)/$', ManageEmployeesView().delete, name="delete_employee")
]
