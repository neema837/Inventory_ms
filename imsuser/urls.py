from django.urls import path
from.import views
urlpatterns = [
    path('userlogin',views.userlogin,name="userlogin"),
    path('userreg',views.userreg, name="userreg"),
    path('userhome',views.userhome, name="userhome"),
    path('userprofile',views.userprofile, name="userprofile"),
    path('userindex<int:cid>',views.userindex, name="userindex"),
    path('viewallprod',views.viewallprod, name="viewallprod"),
    path('prodquickview<int:pid>',views.prodquickview, name="prodquickview"),
    path('prod_by_cat<int:catid>',views.prod_by_cat, name="prod_by_cat"),
    path('productview<int:prodid>',views.productview, name="productview"),
    path('productview<int:prodid>',views.productview, name="productview"),
    path('user_logout',views.user_logout, name="user_logout"),
    path('usercartview',views.usercartview,name="usercartview"),
    path('updatecart',views.updatecart,name="updatecart"),
    path('remove_product<int:rmveid>',views.remove_product, name="remove_product"),
    path('userwishlist',views.userwishlist,name="userwishlist"),
    path('add_to_cart<int:cprdctid>',views.add_to_cart, name="add_to_cart"),
    path('add_to_wishlist<int:wlistid>',views.add_to_wishlist, name="add_to_wishlist"),
    path('remove_wlproduct<int:rmvewlid>',views.remove_wlproduct, name="remove_wlproduct"),
    path('usercheckout',views.usercheckout,name="usercheckout"),
    path('billgeneration',views.billgeneration,name="billgeneration"),



















]
