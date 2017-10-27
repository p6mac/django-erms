from django.conf.urls import url
from login.views import LoginView

urlpatterns = [
    url(r'^$', LoginView().index, name='index'),
    url(r'^logout', LoginView().logout, name="logout"),
    url(r'^register', LoginView().register, name='register')
]

