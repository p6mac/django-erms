from django.conf.urls import url
from .views import ProductsView

urlpatterns = [
    url(r'^manage_products', ProductsView.as_view(), name="manage_products"),
    url(r'^delete_products/(?P<id>\d+)$', ProductsView().delete_product, name='delete_product')
]
