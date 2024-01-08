from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

# Create your models here.

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ip_address

class media(models.Model):
    image = models.ImageField(_('عکس '), upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos_uploaded/',null=True, blank=True,)
    file = models.FileField(upload_to='file/',null=True, blank=True)

class logo(models.Model):
    image = models.ImageField(_('عکس لوگو'), upload_to='logo/')
    date_created = models.DateTimeField(auto_now_add=True)
    
class Category(models.Model):
    name = TranslatedField(models.CharField(_('عنوان'), max_length=100, null=True))
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class customer_comment(models.Model):
    name = TranslatedField(models.CharField(_('نام'), max_length=100, null=True))
    description = TranslatedField(models.TextField(_('توضیحات'), null=True))
    projname = models.CharField(_('اسم پروژه'), max_length=100, blank=True, null=True)

    date = models.DateField(_('تاریخ'))

    def __str__(self):
        return self.name


class Slider(models.Model):
    image = models.ImageField(_('عکس اسلایدر'), upload_to='slider/')
    date_created = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = TranslatedField(models.CharField(_('سوال'), max_length=100, null=True))
    answer = TranslatedField(models.TextField(_('جواب'), null=True))
    date = models.DateField(_('تاریخ'))

    def __str__(self):
        return self.question

class Services(models.Model):
    icon = models.ImageField(upload_to="services/icon/", blank=True, null=True)
    name = TranslatedField(models.CharField(_("نام سرویس"), max_length=100, null=True))
    description = TranslatedField(models.TextField(_("توضیحات"), blank=True, null=True))
    link = models.SlugField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Portfolio_architecture(models.Model):
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True )
    name = TranslatedField(models.CharField(_("نام پروژه"), max_length=100, null=True))
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.SET_NULL, blank=True, null=True)
    description = TranslatedField(RichTextField(_("توضیحات"),config_name="default", blank=True, null=True))
    slug = models.SlugField(_("آدرس اینترنتی"))
    date_created = models.DateTimeField(auto_now_add=False)
    image = models.ImageField(_("تصویر 1"), upload_to='portfolio/', blank=True, null=True)
    image2 = models.ImageField(_("تصویر 2"), upload_to='portfolio/', blank=True, null=True)
    image3 = models.ImageField(_("تصویر 3"), upload_to='portfolio/', blank=True, null=True)
    image4 = models.ImageField(_("تصویر 4"), upload_to='portfolio/', blank=True, null=True)
    image5 = models.ImageField(_("تصویر 5"), upload_to='portfolio/', blank=True, null=True)


    def __str__(self):
        return self.name


class Team(models.Model):
    name = TranslatedField(models.CharField(_("نام کامل"), max_length=100, null=True))
    job = TranslatedField(models.CharField(_("سمت"), max_length=100, blank=True, null=True))
    instagram = models.CharField(_("اینستاگرام"), max_length=100, blank=True, null=True)
    linkedin = models.CharField(_("لینکدین"), max_length=100, blank=True, null=True)
    mobile = models.CharField(_("موبایل"), max_length=100, blank=True, null=True)
    email = models.CharField(_("ایمیل"), max_length=100, blank=True, null=True)
    image = models.ImageField(_("تصویر"), upload_to='team/')

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(_("نام کامل"), max_length=900, blank=True, null=True)
    subject = models.CharField(_(" موضوع "), max_length=3000, blank=True, null=True)
    phone = models.CharField(_(" شماره همراه "), max_length=12, blank=True, null=True)
    description = models.TextField(_("توضیحات"), blank=True, null=True)

    def __str__(self):
        return self.subject
        
class gallery(models.Model):
    name = TranslatedField(models.CharField(_("عنوان "), max_length=100, null=True))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True,null=True)
    image = models.ImageField(_("تصویر"), upload_to='gallery/')

    
    def __str__(self):
        return self.name

class Portfolio_Graphic(models.Model):
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True )
    name = TranslatedField(models.CharField(_("نام پروژه"), max_length=100, null=True))
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.SET_NULL, blank=True, null=True)
    description = TranslatedField(RichTextField(_("توضیحات"),config_name="default", blank=True, null=True))
    slug = models.SlugField(_("آدرس اینترنتی"))
    date_created = models.DateTimeField(auto_now_add=False)
    image = models.ImageField(_("تصویر 1"), upload_to='portfoliog/', blank=True, null=True)
    image2 = models.ImageField(_("تصویر 2"), upload_to='portfoliog/', blank=True, null=True)
    image3 = models.ImageField(_("تصویر 3"), upload_to='portfoliog/', blank=True, null=True)
    image4 = models.ImageField(_("تصویر 4"), upload_to='portfoliog/', blank=True, null=True)
    image5 = models.ImageField(_("تصویر 5"), upload_to='portfoliog/', blank=True, null=True)


    def __str__(self):
        return self.name
        
        
class imagesite(models.Model):
    name = models.CharField(_("نام "), max_length=100)
    img = models.ImageField(_("تصویر"), upload_to='media/site/img', blank=True, null=True)
    video = models.FileField(_("ویدیو"), upload_to='media/products/files', blank=True, null=True)
    def __str__(self):
        return self.name


class contentsite(models.Model):
    name = models.CharField(_("نام "), max_length=100)
    content1 = TranslatedField(models.TextField(_("عنوان 1"), blank=True, null=True))
    content2 = TranslatedField(models.TextField(_("عنوان 2"), blank=True, null=True))
    content3 = TranslatedField(models.TextField(_("عنوان 3"), blank=True, null=True))
    content4 = TranslatedField(models.TextField(_("عنوان 4"), blank=True, null=True))
    def __str__(self):
        return self.name

    

