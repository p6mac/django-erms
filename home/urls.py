from django.conf.urls import url
from home.views import ManageEmployeesView, HomeView

urlpatterns = [
    url(r'^manage_employees/$', HomeView.as_view(), name = 'manage_employees'),    
    url(r'^manage_employees/(?P<status>\w+)/$', HomeView.as_view(), name = 'manage_employees'),    
    # url(r'^manage_employees', ManageEmployeesView().index, name = 'manage_employees'), # old
    url(r'^manage_employee/edit/(?P<id>\d+)/$', ManageEmployeesView().edit, name="edit_employee"),
    url(r'^manage_employee/delete/(?P<id>\d+)/$', ManageEmployeesView().delete, name="delete_employee")
]
