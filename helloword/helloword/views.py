from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
import yaml
from django.views import View
import os
from helloword import settings
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
    FilePath = os.path.join(settings.BASE_DIR, 'static','11.png')
    print('FilePath',FilePath)
    with open(file=FilePath, mode='rb') as f:
        return HttpResponse(content=f, content_type='image/png')
        # return FileResponse(content=f, content_type='image/png')


class ImageView(View):
    def get(self,request):
        FilePath = os.path.join(settings.BASE_DIR,'static', '11.png')
        print('这是一个GET请求')
        with open(file=FilePath, mode='rb') as f:
            return HttpResponse(content=f, content_type='image/png')

    def post(self, request):
        # return HttpResponse('这是post请求')
        # return self.get(request)
        file_obj=request.FILES.get('file',None)
        print(file_obj.name)
        print(file_obj.size)

        files = request.FILES
        print('6666666我在views文件',type(files))
        for key,value in files.items():
            print(777,key)
            print(888,value)
        return HttpResponse('测试.123..')


class ImageView1(View):
    def get(self,request):
        FilePath = os.path.join(settings.BASE_DIR, 'static', '11.png')
        print('这是一个GET请求')
        with open(file=FilePath, mode='rb') as f:
            return HttpResponse(content=f, content_type='image/png',text='nihao')
