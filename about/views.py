from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from product.models import Product, ProductCategory, Employees, Offers

class aboutView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = {}


        employees = Employees.objects.all()

        context['employees'] =employees

        return context

