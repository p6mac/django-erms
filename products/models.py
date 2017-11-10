from django.db import models
from django.forms import ModelForm
import os
# Create your models here.
def custom_filename(instance, filename) :
    file_ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.product_name, file_ext)
    return os.path.join('products', filename)

class Products(models.Model) :
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image_url = models.FileField(upload_to=custom_filename, null=True)

    class Meta :
        db_table = 'products'

class ProductsForm(ModelForm) :
    class Meta :
        model = Products
        fields = '__all__'

