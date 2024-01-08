from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import MyUser
from . import forms
from . import helper
from core.models import imagesite
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout



@csrf_exempt 
def register_view(request):
    logo = imagesite.objects.get(id=1)
    form = forms.RegisterForm()

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                # send otp
                otp = helper.get_random_otp()
                helper.send_otp(mobile, otp)
                # helper.send_otp_soap(mobile, otp)
                # save otp
                # print(otp)
                user.otp = otp
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse_lazy('customuser:verify'))

        except MyUser.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # send otp
                otp = helper.get_random_otp()
                helper.send_otp(mobile, otp)
                # helper.send_otp_soap(mobile, otp)
                # save otp
                # print(otp)
                user.otp = otp
                user.is_active = True
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse_lazy('customuser:verify'))
    return render(request, 'login.html', {'form': form, "logo": logo})


def verify(request):
    logo = imagesite.objects.get(id=1)
    try:
        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile = mobile)
       
        if request.method == "POST":

            # check otp expiration
            # if not helper.check_otp_expiration(user.mobile):
            #     messages.error(request, "OTP is expired, please try again.")
            #     return HttpResponseRedirect(reverse_lazy('customuser:register_view'))

            if user.otp != int(request.POST.get('otp')):
                return HttpResponseRedirect(reverse_lazy('customuser:verify'))
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('core:home'))

        return render(request, 'otp.html', {'mobile': mobile, "logo": logo})

    except MyUser.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('customuser:register_view'))
        
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('core:home'))
