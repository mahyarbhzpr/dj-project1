from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=11)
    description = forms.CharField(widget=forms.Textarea)