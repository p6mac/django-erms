from django.conf.urls import url
from .views import ShoppingView

urlpatterns = [
    url(r'^shopping$', ShoppingView.as_view(), name='shopping_cart')
]