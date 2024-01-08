from django.db import models

# Create your models here.

class Custom_Js(models.Model):
    name = models.CharField(max_length=100)
    custom_js = models.TextField(help_text='Custom JavaScript')
    def __str__(self):return self.name
    
class CustomCss(models.Model):
    name = models.CharField(max_length=100)
    custom_css = models.TextField(help_text='Custom Css')
    def __str__(self):return self.name

