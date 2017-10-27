from django.conf.urls import url
from departments.views import DepartmentsView
urlpatterns = [
    url(r'^manage_departments', DepartmentsView.as_view(), name='manage_departments')
]
