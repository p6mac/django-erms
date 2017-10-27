from django.conf.urls import url
from users.views import UsersView

urlpatterns = [
    url(r'^manage_users', UsersView().index, name ="manage_users"),
    url(r'^manage_user/delete/(?P<id>\d+)/$', UsersView().delete, name="delete_user")
]