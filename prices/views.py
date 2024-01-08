from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PriceMeter
from .models import *
from customuser.models import MyUser
from core.models import contentsite
# Create your views here.
@login_required
def PriceMeterView(request):
    question1 = contentsite.objects.get(id=18)
    question2 = contentsite.objects.get(id=19)
    question3 = contentsite.objects.get(id=20)
    question4 = contentsite.objects.get(id=21)
    question5 = contentsite.objects.get(id=22)
    question6 = contentsite.objects.get(id=23)
    question7 = contentsite.objects.get(id=24)
    questionv1 = Question1.objects.all()
    questionv2 = Question2.objects.all()
    questionv4 = Question4.objects.all()
    questionv5 = Question5.objects.all()
    questionv6 = Question6.objects.all()
    questionv7 = Question7.objects.all()
    questionv10 = Question10.objects.all()
    questionv11 = Question11.objects.all()
    questionv12 = Question12.objects.all()
    questionv13 = Question13.objects.all()
    questionv14 = Question14.objects.all()
    questionv15 = Question15.objects.all()
    questionv16 = Question16.objects.all()
    questionv17 = Question17.objects.all()
    questionv18 = Question18.objects.all()
    questionv20 = Question20.objects.all()
    questionv25 = Question25.objects.all()
    questionv26 = Question26.objects.all()
    questionv27 = Question27.objects.all()
    

    if request.method == "POST":
        form = PriceMeter(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:dashboard")
    else:
        form = PriceMeter()
    # pmeter1 = Question1.objects.get(pk=request.POST.get('price'))
    return render(request, "pricemeter/forms.html", {"form": form,
                                          'questionv1': questionv1,'questionv2': questionv2,
                                          'questionv4': questionv4,
                                          'questionv5': questionv5,'questionv6': questionv6,
                                          'questionv7': questionv7,
                                          'questionv10': questionv10,
                                          'questionv11': questionv11,'questionv12': questionv12,
                                          'questionv13': questionv13,'questionv14': questionv14,
                                          'questionv15': questionv15,'questionv16': questionv16,
                                          'questionv17': questionv17, 'questionv18': questionv18,
                                         'questionv20': questionv20,
                                          'questionv25': questionv25, 'questionv26': questionv26,
                                          'questionv27': questionv27,
                                          'question1':question1,
                                          'question2':question2,
                                          'question3':question3,
                                          'question4':question4,
                                          'question5':question5,
                                          'question6':question6,
                                          'question7':question7,
                                          })

