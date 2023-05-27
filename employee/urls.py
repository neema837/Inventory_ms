from django.urls import path
from.import views
urlpatterns = [
    path('employlogin',views.employlogin,name="employlogin"),
    path('emphome',views.emphome,name="emphome"),
    path('eaddprod',views.eaddprod,name="eaddprod"),
    path('addcat',views.addcat,name="addcat"),
    path('eviewprod',views.eviewprod,name="eviewprod"),
    path('eviewoneprod<int:pid>',views.eviewoneprod,name="eviewoneprod"),
    path('eupdateprod<int:pid>',views.eupdateprod,name="eupdateprod"),
    path('edeleteprod<int:did>',views.edeleteprod,name="edeleteprod"),
    path('prod_by_cat<str:cid>',views.prod_by_cat,name="prod_by_cat"),
    path('emp_logout',views.emp_logout,name="emp_logout"),






]
