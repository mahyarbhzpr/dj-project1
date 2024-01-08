from django.urls import path
from .views import *
app_name = 'prices'

urlpatterns = [
    path("", PriceMeterView, name="prices"),
    # path("p/", price_view, name="price_view")
]