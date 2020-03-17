from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
import yaml
from django.views import View
import os
from helloword import settings
import json
import requests
from helloword import secret_setshezhi
from juheapp import models


def index(request):
    return HttpResponse("Hello,world.首页")


def page_not_found(request, exception):
    return render(request, 'not_fonudhtml.html')


# def apps(request):  # 传递列表
#     return JsonResponse(['微信','支付宝'],safe=False)

# def apps(request):  # 传递字典
#     return JsonResponse({'name':['微信','支付宝','钉钉']},safe=True)

# def apps(request):  # 传递列表套字典
#     return JsonResponse([{'name': '微信'}, {'name': '支付宝'}, {'name': '钉钉'}], safe=False)


def apps(request):
    filepath = r'D:\pychar\Djangostudy\helloword\helloword\myappconfig.yaml'
    with open(filepath, 'r', encoding='utf8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        return JsonResponse(res)


def get_image(request):
    FilePath = os.path.join(settings.BASE_DIR, 'static', '11.png')
    print('FilePath', FilePath)
    with open(file=FilePath, mode='rb') as f:
        return HttpResponse(content=f, content_type='image/png')
        # return FileResponse(content=f, content_type='image/png')


class ImageView(View):
    def get(self, request):
        FilePath = os.path.join(settings.BASE_DIR, 'static', '11.png')
        print('这是一个GET请求')
        with open(file=FilePath, mode='rb') as f:
            return HttpResponse(content=f, content_type='image/png')

    def post(self, request):
        # return HttpResponse('这是post请求')
        # return self.get(request)
        file_obj = request.FILES.get('file', None)
        print(file_obj.name)
        print(file_obj.size)

        files = request.FILES
        print('6666666我在views文件', type(files))
        for key, value in files.items():
            print(777, key)
            print(888, value)
        return HttpResponse('测试.123..')


class ImageView1(View):
    def get(self, request):
        FilePath = os.path.join(settings.BASE_DIR, 'static', '11.png')
        print('这是一个GET请求')
        with open(file=FilePath, mode='rb') as f:
            return HttpResponse(content=f, content_type='image/png', text='nihao')


class CookieTest(View):
    # 发送数据
    def get(self, request):
        # print(dir(request))
        request.session['mykey'] = '我的值'
        return JsonResponse({'key': 'value'})


class CookieTest2(View):
    """
    这个视图负责接收cookie
    这是视图是由cookieTest复制而来
    """

    def get(self, request):
        # print(dir(request))
        print('11111', request.session['mykey'])
        print(request.session.items())
        return JsonResponse({'key2': 'value2'})


class Authorize(View):
    def get(self, request):
        return HttpResponse('请求不支持GET方法')

    def post(self, request):
        bodystr = request.body.decode('utf-8')
        bodydict = json.loads(bodystr)
        code = bodydict.get('code')
        userinfo = bodydict.get('nackname')
        print(code)
        print(userinfo)
        appid = secret_setshezhi.APPID
        secret = secret_setshezhi.SECTER_KEY
        # 发起请求
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + appid + '&secret=' + secret + '&js_code=' + code + '&grant_type=authorization_code'
        res = requests.get(url)
        res_dict = json.loads(res.text)
        print('res_dict', res_dict)
        openid = res_dict.get('openid')
        print('openid', openid)
        print('res_dict', res_dict)
        if not openid:
            return HttpResponse('失败')
        # 给这个用户赋予了一些状态
        request.session['openid'] = openid
        request.session['id_authorized'] = True
        # 将用户保存到数据库中
        if not models.User.objects.filter(openid=openid):
            new_user = models.User(openid=openid, nickname=userinfo)
            new_user.save()
        return HttpResponse('成功')

    # 打开小程序   ?????????


# 判断是否已经授权
def already_authorized(request):
    is_authorized = False
    if request.session.get('is_authorized'):
        is_authorized = True
    return is_authorized


class UserView(View):

    # 关注的城市、股票和星座
    def get(self, request):
        if not already_authorized(request):
            return JsonResponse({'key': '没登录认证'}, safe=False)
        openid = request.session.get('openid')
        print(openid, 'openid-----------------')
        user = models.User.objects.get(openid=openid)
        data = {}
        data['focus'] = {}
        data['focus']['city'] = json.loads(user.city)
        data['focus']['stock'] = json.loads(user.stock)
        data['focus']['constellation'] = json.loads(user.constellation)
        print(data, '-*****************')
        return JsonResponse(data=data, safe=False)

    def post(self, request):
        if not already_authorized(request):
            return JsonResponse({'key': '没登录认证'}, safe=False)
        openid = request.session.get('openid')
        # print('openid',openid)
        # 从数据库获取到openid
        user = models.User.objects.get(openid=openid)
        # 解码获取到的body的内容
        received_body = request.body.decode('utf-8')
        # 转换为字典
        received_body = eval(received_body)
        cities = received_body.get('city')
        stocks = received_body.get('stock')
        constellations = received_body.get('constellation')
        # print({'received_body':received_body})

        #  不是追加的形式,是覆盖原有纪录

        #     以json格式存入数据库
        if cities:
            user.city = json.dumps(cities)
            # user.city = cities
            user.save()
        elif stocks:
            user.stock = json.dumps(stocks)
            # user.stock = stocks
            user.save()
        elif constellations:
            user.constellation = json.dumps(constellations)
            # user.constellation = constellations
            user.save()
        else:
            return HttpResponse('获取到的{}为空'.format(cities, stocks, constellations))
        # 类名.objects.get(pk=id)
        u = models.User.objects.get(openid=openid)
        print(u.city, u.stock, u.constellation)
        return JsonResponse(data={'msg': '成功了'}, safe=False)


class Logout(View):
    def get(self, request):
        request.session.clear()
        return JsonResponse(data={"status": "Logout"}, safe=False)


class Status(View):
    def get(self, request):
        if already_authorized(request):
            data = ({'is_authorized': 1})
        else:
            data = ({'is_authorized': 0})
        return JsonResponse(data=data, safe=False)
