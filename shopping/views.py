from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Products
# Create your views here.
class ShoppingView(TemplateView):
    template_name = 'shoppingTpl.html'

    def get(self, request):
        context = {
            'account_name' : request.session.get('username'),
            'products' : Products.objects.all()
        }
        return render(request, self.template_name, context)