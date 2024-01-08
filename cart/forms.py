from django import forms
class CartAddProductForm(forms.Form):
    product_count = forms.IntegerField(max_value=9)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)