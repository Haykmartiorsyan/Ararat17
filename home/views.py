from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from product.models import Product, ProductCategory, Gallery, GalleryImage, Offers
# Create your views here.

class homeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        products = Product.objects.filter(is_active=True)
        categories = ProductCategory.objects.all()
        gallery_image = GalleryImage.objects.filter(is_active=True)
        offers = Offers.objects.all()


        context['products'] = products
        context['categories'] = categories
        context['gallery_image'] = gallery_image
        context['offers'] = offers

        return context


