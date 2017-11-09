from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Products, ProductsForm
# Create your views here.
class ProductsView(TemplateView):
    template_name = 'manage_products.html'


    def get(self, request) :
        context = {
            'account_name' : request.session.get('username'),
            'products' : Products.objects.all()
        }
        print(Products.objects.all())
        return render(request, self.template_name, context)

    def post(self, request) :
        form = ProductsForm(request.POST)

        if form.is_valid() :
            form.save()
        
        return redirect('/manage_products')
    
    def delete_product(self, request, id=None):
        Products.objects.filter(pk=id).delete()
        return redirect('/manage_products')


class ManageProductsView :
    def edit(self, request, id) :
        pass
    
    # def delete