from django.shortcuts import render
from django.http import HttpResponse
import requests
from helloword import settings
# Create your views here.


def hello_juhe(request):
    url = 'http://v.juhe.cn/joke/content/list.php?sort=asc&page=3&pagesize=3&time=1418816972&key=265e5edbc0f1cf02b5dba5788963a771'
    res = requests.get(url)
    if res.status_code == 200:
        return HttpResponse(res.text)
    else:
        return HttpResponse('没有找到数据')

