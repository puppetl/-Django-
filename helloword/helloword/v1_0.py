from django.urls import path,include
from helloword import views
urlpatterns = [
    path('jokes/', include('juheapp.urls')),
    path('apps/', views.apps),
    path('testcookie/', views.CookieTest.as_view()),########
    path('testcookie2/', views.CookieTest2.as_view()),
    path('testcookie3/', views.Authorize.as_view()),
    path('authorize/', views.Authorize.as_view()),
    path('userview/', views.UserView.as_view()),
    path('logout/', views.Logout.as_view()),
    path('status/', views.Status.as_view())


]