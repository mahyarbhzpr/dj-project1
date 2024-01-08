from django.contrib import admin
from .models import *
# Register your models here.

class imgsite(admin.ModelAdmin):
    list_display = ("name", "id", "img")

class contsite(admin.ModelAdmin):
    list_display = ("name", "id", "content1")

class IpUser(admin.ModelAdmin):
    list_display = ("id", "ip_address", "date_created")

admin.site.register(Slider)
admin.site.register(Portfolio_Graphic)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(customer_comment)
admin.site.register(FAQ)
admin.site.register(Team)
admin.site.register(Contacts)
admin.site.register(Portfolio_architecture)
admin.site.register(logo)
admin.site.register(media)
admin.site.register(gallery)
admin.site.register(contentsite, contsite)
admin.site.register(imagesite, imgsite)
admin.site.register(IPAddress, IpUser)