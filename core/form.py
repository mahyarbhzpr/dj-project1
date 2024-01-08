from .models import Contacts
from django import forms
from django import forms
from customuser import models


class dashboarduser(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['full_name', 'image']


class contacts(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"
