from .models import PriceMeterForm
from django.forms import ModelForm


class PriceMeter(ModelForm):
    class Meta:
        model = PriceMeterForm
        fields = '__all__'

