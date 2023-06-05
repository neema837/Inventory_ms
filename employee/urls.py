from django.urls import path
from.import views
urlpatterns = [
    path('employlogin',views.employlogin,name="employlogin"),

    path('supervisorhome',views.supervisorhome,name="supervisorhome"),
    path('supervisoraddtask',views.supervisoraddtask,name="supervisoraddtask"),
    path('supervisorviewtask',views.supervisorviewtask,name="supervisorviewtask"),



    path('emphome',views.emphome,name="emphome"),
    path('eaddprod',views.eaddprod,name="eaddprod"),
    path('addcat',views.addcat,name="addcat"),
    path('eviewprod',views.eviewprod,name="eviewprod"),
    path('eviewoneprod<int:pid>',views.eviewoneprod,name="eviewoneprod"),
    path('eupdateprod<int:pid>',views.eupdateprod,name="eupdateprod"),
    path('edeleteprod<int:did>',views.edeleteprod,name="edeleteprod"),
    path('eprod_by_cat<str:cid>',views.eprod_by_cat,name="eprod_by_cat"),
    
    path('eviewsupp',views.eviewsupp,name="eviewsupp"),
    path('eviewspproducts<int:spid>',views.eviewspproducts,name="eviewspproducts"),
    path('esplrprod_by_cat<int:catid>',views.esplrprod_by_cat,name="esplrprod_by_cat"),
    path('purchases',views.purchases,name="purchases"),
    path('createrfq<int:spid>',views.createrfq,name="createrfq"),
    path('get-product-price/', views.get_product_price, name='get_product_price'),
    path('purchasepayment<int:orderid>',views.purchasepayment,name="purchasepayment"),

    



    path('emp_logout',views.emp_logout,name="emp_logout"),






]
