from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    index = models.IntegerField(default=1)
    image = models.ImageField(upload_to='slider_image')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return "%s" %  self.name



class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    productcategory = models.ManyToManyField(ProductCategory, 'self', null=True, blank=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', blank=True, null=True, default=None)
    image = models.ImageField(upload_to="product_image")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

class Employees(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    index = models.IntegerField(default=1)
    image = models.ImageField(upload_to='employees_image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

class Offers(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to="services_image")
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

class Gallery(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', blank=True, null=True, default=None)
    image = models.ImageField(upload_to="gallery_images")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"


class Catering(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=64)
    details = models.TextField()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Catering Message"
        verbose_name_plural = "Catering Messages"





