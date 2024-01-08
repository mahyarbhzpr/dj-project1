from django.contrib import admin
from .models import *
# Register your models here.
class prd(admin.ModelAdmin):
    list_display = ("id", "name", "date_created")

admin.site.register(Category)
admin.site.register(slider)
admin.site.register(Product,prd )
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Invoice)
admin.site.register(Transaction)
admin.site.register(UserProduct)
admin.site.register(ShopComment)