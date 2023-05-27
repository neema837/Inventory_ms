from django.urls import path
from.import views
urlpatterns = [
    path('supplogin',views.supplogin,name="supplogin"),
    path('suppreg',views.suppreg, name="suppreg"),
    path('supphome',views.supphome, name="supphome"),
    path('saddprod',views.saddprod, name="saddprod"),
    path('saddcat',views.saddcat, name="saddcat"),
    path('sviewprod',views.sviewprod, name="sviewprod"),
    path('sviewoneprod<int:spid>',views.sviewoneprod, name="sviewoneprod"),
    path('supdateprod<int:upid>',views.supdateprod,name="supdateprod"),
    path('sdeleteprod<int:dpid>',views.sdeleteprod,name="sdeleteprod"),








]
