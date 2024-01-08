from django.urls import path
from .views import customcss

app_name = 'blog'

urlpatterns = [
    path('', customcss, name='css'),
]

