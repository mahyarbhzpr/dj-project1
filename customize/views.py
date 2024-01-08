from django.shortcuts import render
from .models import *
# Create your views here.
def customjs(request):
    js = Custom_Js.objects.all()
    return render(request, 'js.html', {'js': js})
def customcss(request):
    css = CustomCss.objects.all()
    return render(request, 'style.html', context={'css': css})