from random import randint
from .melipayamak.melipayamak import Api
from zeep import Client
from . import models
import datetime
import time


def send_otp(mobile, otp):
    mobile = [mobile]
    username = '09197555359'
    password = '!SPYO'
    api = Api(username, password)
    sms = api.sms()
    to = mobile
    _from = '50004001555359'
    text = 'به روخام خوش آمدید \n کد تایید شما :{} \n https://rokhaam.com'.format(otp)
    response = sms.send(to, _from, text)
    print(response)


def get_random_otp():
    return randint(1000, 9999)


def check_otp_expiration(mobile):
    try:
        user = models.MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now.minute - otp_time.minute
        if diff_time > 4:
            return False
        else:
            return True

    except models.MyUser.DoesNotExist:
        return False
