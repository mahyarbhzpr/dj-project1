from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(keyword)
admin.site.register(blogComment)