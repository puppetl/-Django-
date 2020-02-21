from django.urls import path,include
from helloword import views
urlpatterns = [
    path('jokes/', include('juheapp.urls')),
    path('apps/', views.apps),
]