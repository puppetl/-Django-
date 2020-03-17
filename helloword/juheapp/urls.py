from django.urls import path,include
from juheapp import views

urlpatterns = [
    path('juhe/',views.hello_juhe),
    path('joke/',views.hello_juhe),
]