from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from core.models import IPAddress
from translated_fields import TranslatedField


# Create your models here.


class Category(models.Model):
    title = TranslatedField(models.CharField(_("عنوان"), max_length=50))
    slug = models.SlugField(_("آدرس اینترنتی (لاتین)"))
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = TranslatedField(models.CharField(_("عنوان"), max_length=50))
    slug = models.SlugField(_("آدرس اینترنتی (لاتین)"))

    def __str__(self):
        return self.title


class keyword(models.Model):
    name = TranslatedField(models.CharField(_("عنوان"), max_length=500))

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("نویسنده"))
    image = models.ImageField(_("عکس"), upload_to='posts/')
    title = TranslatedField(models.CharField(_("عنوان"), max_length=500))
    category = models.ManyToManyField(Category, blank=True, verbose_name=_("دسته بندی"), related_name="categories")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("برچسب ها"), related_name="tag")
    description = TranslatedField(RichTextField(_("توضیحات"), config_name="default"))
    keyword = models.ManyToManyField(keyword, blank=True, verbose_name=_("کلمات کلیدی"), related_name='keyword', null=True)
    author_comment = TranslatedField(models.TextField(_("خلاصه نظر نویسنده"), blank=True, null=True))
    meta_description = TranslatedField(models.TextField(_("توضیحات متا سئو"), blank=True, null=True))
    slug = models.SlugField(_(" آدرس اینترنتی "))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class blogComment(models.Model):
    blog = models.ForeignKey(Post, verbose_name=_("پست"), related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    phone = models.CharField(_("شماره تلفن همراه"), max_length=11)
    description = models.TextField(_("توضیحات"))
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name