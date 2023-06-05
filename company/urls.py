from django.urls import path
from.import views
urlpatterns = [
    path('comlogin',views.comlogin,name="comlogin"),
    path('comreg',views.comreg,name="comreg"),
    path('comhome',views.comhome,name="comhome"),
    path('caddemploy',views.caddemploy,name="caddemploy"),
    path('cviewemploy',views.cviewemploy,name="cviewemploy"),
    path('send_empmail<int:eid> ',views.send_empmail,name="send_empmail"),
    path('cviewsuppliers',views.cviewsuppliers,name="cviewsuppliers"),
    path('viewspproducts<int:sid>',views.viewspproducts, name="viewspproducts"),
    path('sprod_by_cat<int:catid>',views.sprod_by_cat,name="sprod_by_cat"),
    

    





    




    
]
