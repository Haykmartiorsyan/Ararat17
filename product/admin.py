from django.contrib import admin
from .models import *


admin.site.register(ProductCategory)
admin.site.register(Slider)
admin.site.register(ProductImage)
admin.site.register(Employees)
admin.site.register(Contact)
admin.site.register(Offers)
admin.site.register(Catering)

# Product Images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

# Menu
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0

class GalleryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gallery._meta.fields]
    inlines = [GalleryImageInline]
    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)