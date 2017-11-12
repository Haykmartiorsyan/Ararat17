
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from product.models import Product, ProductCategory

class menuView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        categories = ProductCategory.objects.all()
        products = Product.objects.filter(is_active=True)

        context['categories'] = categories
        context['products'] = products



        return context

class singleItem(generic.DetailView):
    template_name = 'menu/single.html'


    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(singleItem, self).get_context_data(**kwargs)



        return context


