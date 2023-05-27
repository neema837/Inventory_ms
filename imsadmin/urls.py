from django.urls import path
from.import views
urlpatterns = [
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminreg',views.adminreg,name="adminreg"),
    path('adhome',views.adhome,name="adhome"),
    
    path('companies',views.companies,name="companies"),
    path('capprove<int:id>',views.capprove,name="capprove"),
    path('creject<int:id>',views.creject,name="creject"),
    path('send_cmail<int:id>',views.send_cmail,name="send_cmail"),
    path('send_crejmail<int:id>',views.send_crejmail,name="send_crejmail"),

    path('suppliers',views.suppliers,name="suppliers"),
    path('sapprove<int:id>',views.sapprove,name="sapprove"),
    path('sreject<int:id>',views.sreject,name="sreject"),
    path('send_smail<int:id>',views.send_smail,name="send_smail"),
    path('send_srejmail<int:id>',views.send_srejmail,name="send_srejmail"),

    





    




]
