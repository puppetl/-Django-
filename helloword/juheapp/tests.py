from django.test import TestCase

# Create your tests here.
import yaml
from juheapp import models
filepath = r'D:\pychar\Djangostudy\helloword\helloword\myappconfig.yaml'
with open(filepath, 'r', encoding='utf8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)

# from juheapp.models import User
# User.objects.create(openid=123,nickname='zhansan',citys=['北京'],stocks=['123'],constellations=['wotm'])


def add_one():
    user = models.User(openid='test_opend',nickname='test_nickname')
    user.save()


add_one()







