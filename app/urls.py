from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('reg',views.reg,name="reg"),
    path('home',views.home,name="home"),




]