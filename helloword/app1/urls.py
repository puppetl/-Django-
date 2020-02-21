from django.urls import path
from app1 import views
urlpatterns = [
    path('hello/', views.index),  # 2.10课程
    path('show_aticle/', views.show_aticle),  # 主页面
    path('show/<int:article_id>', views.bigso),  # 显示详情页,是url地之栏里面输入
    #  <int:article_id> 是用来获取地址栏中的page
]