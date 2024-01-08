from django.contrib.auth.models import User
from django.conf import settings

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Question1(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question2(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question4(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question5(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question6(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question7(models.Model):
    city = models.ForeignKey(Question6, on_delete=models.SET_NULL,blank=True, null=True)
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question10(models.Model):
    image = models.ImageField(upload_to="images/pricemeter/", blank=True, null=True)
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question11(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question12(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question13(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question14(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question15(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question16(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question17(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question18(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name



class Question20(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question25(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question26(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Question27(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class PriceMeterForm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    question1 = models.ForeignKey(Question1, on_delete=models.SET_NULL,blank=True, null=True)
    question2 = models.ForeignKey(Question2, on_delete=models.SET_NULL,blank=True, null=True)
    question3 = models.IntegerField(default=1, blank=True, null=True)
    question4 = models.ForeignKey(Question4, on_delete=models.SET_NULL,blank=True, null=True)
    question5 = models.ForeignKey(Question5, on_delete=models.SET_NULL,blank=True, null=True)
    question6 = models.ForeignKey(Question6, on_delete=models.SET_NULL,blank=True, null=True)
    question7 = models.ForeignKey(Question7, on_delete=models.SET_NULL,blank=True, null=True)
    question8 = models.IntegerField(default=1, blank=True, null=True)
    question9 = models.IntegerField(default=1, blank=True, null=True)
    question10 = models.ForeignKey(Question10, on_delete=models.SET_NULL,blank=True, null=True)
    question11 = models.ForeignKey(Question11, on_delete=models.SET_NULL,blank=True, null=True)
    question12 = models.ForeignKey(Question12, on_delete=models.SET_NULL,blank=True, null=True)
    question13 = models.ForeignKey(Question13, on_delete=models.SET_NULL,blank=True, null=True)
    question14 = models.ForeignKey(Question14, on_delete=models.SET_NULL,blank=True, null=True)
    question15 = models.ForeignKey(Question15, on_delete=models.SET_NULL,blank=True, null=True)
    question16 = models.ForeignKey(Question16, on_delete=models.SET_NULL,blank=True, null=True)
    question17 = models.ForeignKey(Question17, on_delete=models.SET_NULL,blank=True, null=True)
    question18 = models.ForeignKey(Question18, on_delete=models.SET_NULL,blank=True, null=True)
    question19 = models.IntegerField(default=1, blank=True, null=True)
    question20 = models.ForeignKey(Question20, on_delete=models.SET_NULL,blank=True, null=True)
    question21 = models.IntegerField(default=1, blank=True, null=True)
    question22 = models.IntegerField(default=1, blank=True, null=True)
    question23 = models.IntegerField(default=1, blank=True, null=True)
    question24 = models.IntegerField(default=1, blank=True, null=True)
    question25 = models.ForeignKey(Question25, on_delete=models.SET_NULL,blank=True, null=True)
    question26 = models.ForeignKey(Question26, on_delete=models.SET_NULL,blank=True, null=True)
    question27 = models.ForeignKey(Question27, on_delete=models.SET_NULL,blank=True, null=True)
    question28 = models.IntegerField(default=1, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank=True)
    rates = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user
    