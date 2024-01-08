from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "shop"

urlpatterns = [
    path("", product_list, name="products"),
    path("mostbought/", product_listbuy, name="productsbuy"),
    path("popular/", product_listpopular, name="productspopular"),
    path("mostview/", product_listmostview, name="productsmostview"),
    path('product/<slug>/', product_details, name="product_details"),
    path('checkout/', checkout, name="checkout"),
    path('to-bank/<int:order_id>/', to_bank, name='to_bank'),
    path('callback/', callback, name='callback'),
    path('category/<slug>/', products_category, name='product_category'),
    path('stores/', Search, name='searchstores'),
    path('download/<slug>', download_file, name='downlaod')
]