from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
from ckeditor.fields import RichTextField
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation
from core.models import IPAddress
from translated_fields import TranslatedField


# Create your models here.
class slider(models.Model):
    image = models.ImageField(upload_to='product_slider/%y/%m/%d/', blank=True, null=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    image = models.ImageField(upload_to='category/%y/%m/%d/', blank=True, null=True)
    name = TranslatedField(models.CharField(max_length=100, null=True))
    slug = models.SlugField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = TranslatedField(models.CharField(max_length=100, null=True))
    image = models.ImageField(upload_to='images/product/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='images/product/%y/%m/%d', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/product/%y/%m/%d', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/product/%y/%m/%d', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/product/%y/%m/%d', blank=True, null=True)
    short_description = TranslatedField(models.TextField(blank=True, null=True))
    keywords = TranslatedField(models.TextField(blank=True, null=True, help_text="با کاما (,) جدا شود"))
    description = TranslatedField(RichTextField(config_name="default"))
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    file = models.FileField(upload_to='media/products/files')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    discount = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField()
    ratings = GenericRelation(Rating, related_query_name='ratings')
    countofbuy = models.IntegerField(blank=True, null=True, default=0)
    viewscount=models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("shop:product_details", args=[self.slug])


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer.mobile
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    product_total = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return self.product.name


class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    authority = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('completed', 'Completed'),
              )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return str(self.id)
        
class UserProduct(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'user={self.user}, product={self.product}'
        
class ShopComment(models.Model):
    product = models.ForeignKey(Product, verbose_name='shop', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name