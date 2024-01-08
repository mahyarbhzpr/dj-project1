from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('search/', Search, name='search'),
    path('', BlogsView, name='blogs'),
    path('<slug>/', BlogDetailView, name='blog_detail'),
    path('tag/<slug>/', blog_tag, name='blog_tag'),
    path('category/<slug>/', blog_category, name='blog_category'),
]

