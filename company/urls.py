from django.urls import path
from.import views
urlpatterns = [
    path('comlogin',views.comlogin,name="comlogin"),
    path('comreg',views.comreg,name="comreg"),
    path('comhome',views.comhome,name="comhome"),
    path('caddemploy',views.caddemploy,name="caddemploy"),
    path('send_empmail<int:eid> ',views.send_empmail,name="send_empmail"),


    




    
]
