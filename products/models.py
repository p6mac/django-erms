from django.db import models
from django.forms import ModelForm
# Create your models here.
class Products(models.Model) :
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta :
        db_table = 'products'

class ProductsForm(ModelForm) :
    class Meta :
        model = Products
        fields = '__all__'