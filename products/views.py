from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Products, ProductsForm
from django.http import HttpResponse
import xlwt

# Create your views here.
class ProductsView(TemplateView):
    template_name = 'manage_products.html'


    def get(self, request) :
        context = {
            'account_name' : request.session.get('username'),
            'products' : Products.objects.all()
        }
        print(Products.objects.all().values_list('product_name'))
        return render(request, self.template_name, context)

    def post(self, request) :
        form = ProductsForm(request.POST, request.FILES)

        if form.is_valid() :
            form.save()
        else :
            print(form.errors)
        
        return redirect('/manage_products')
    
    def delete_product(self, request, id=None):
        Products.objects.filter(pk=id).delete()
        return redirect('/manage_products')


class GenerateProductsReports() :
    def generate_product_xlsx(self, request) :
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="products.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Products')

        row_num = 1

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Product Name', 'Category', 'Price', 'Quantity']

        ws.write_merge(0,0,0,4, 'The Quick Brown Fox Jumps Over The Lazy Dog')               
        for col_num in range(len(columns)) :
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        rows = Products.objects.values_list('id', 'product_name', 'category', 'price', 'quantity')
        for row in rows :
            row_num += 1
            for col_num in range(len(row)) :
                ws.write(row_num, col_num, row[col_num], font_style)
                
        wb.save(response)
        return response 

        
