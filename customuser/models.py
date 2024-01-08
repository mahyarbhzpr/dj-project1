# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .myusermanager import MyUserManager


class MyUser(AbstractUser):
    username = None
    # password = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="admin/images/team/", blank=True, null=True)
    mobile = models.CharField(max_length=11, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'
    # PASSWORD_FIELD = 'password'

    REQUIRED_FIELDS = []

    backend = 'customuser.mybackend.ModelBackend'
    
    def __str__(self):
        return str(self.full_name)