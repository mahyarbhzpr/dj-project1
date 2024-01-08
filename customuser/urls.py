from django.urls import path
from . import views

app_name="customuser"

urlpatterns = [
    path('login/', views.register_view, name='register_view'),
    path('verify/', views.verify, name='verify'),
    path('logout/', views.logout_view, name='logout'),
]