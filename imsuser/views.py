from django.shortcuts import *
from django.urls import reverse
from.models import*
from django.http import*
from django.contrib import messages
from employee.models import*
from company.models import*
from IMS.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
import random,string


# Create your views here.

def userlogin(request):
    if request.method=='POST':
        try:
            umail=request.POST['umail']
            upwd=request.POST['upwd']
            check=Customers.objects.get(umail=umail,upwd=upwd)
            request.session['userid']=check.id
            sid=request.session['userid']
            print(sid)
            request.session['umail']=check.umail
            return redirect('userhome')
        except Customers.DoesNotExist as e:
            messages.info(request,"invalid user")
    return render(request,'imsuser/userlogin.html')

def user_logout(request):
    del request.session['userid']
    return redirect('index')



def userreg(request):
   if request.method=='POST':
        uname=request.POST['uname']
        umail=request.POST['umail']
        uphone=request.POST['uphone']
        uimage=request.FILES.get('uimage')
        uaddr=request.POST['uaddr']
        ucity=request.POST['ucity']
        uzip=request.POST['uzip']
        ustate=request.POST['ustate']
        ucountry=request.POST['ucountry']
        #utype=request.POST['utype']
        #ucompany=request.POST['ucompany']
        upwd=request.POST['upwd']
        cpwd=request.POST['cpwd']
        if upwd==cpwd:
            if Customers.objects.filter(umail=umail):
                messages.info(request,"This email id is existing already")
            else:
                saveval=Customers(uname=uname,umail=umail,uphone=uphone,uimage=uimage,
                                  uaddr=uaddr,ucity=ucity,uzip=uzip,ustate=ustate,
                                  ucountry=ucountry,upwd=upwd)
                saveval.save()
        else:
            messages.info(request,"password doesn't match")
   return render(request,'imsuser/userreg.html')

   
def userhome(request):
    cmpdetails=Companies.objects.all()
    """ print(request.session['userid']) """
    context={
             'cmpdetails':cmpdetails
        }
    return render(request,'imsuser/userhome.html',context)


def userprofile(request):
    return render(request,'imsuser/userprofile.html')


def userindex(request,cid):
    request.session['cid'] = cid
    userid= request.session['userid']
    items = Cart.objects.filter(uid_id=userid)
    witems = WishList.objects.filter(uid_id=userid,status=True)
    cmpny=Companies.objects.get(id=cid)
    print(cmpny.cpname)
    pcat=ProductCategory.objects.filter(cmpid=cid)
    cprod=Product.objects.filter(cmpid=cid)
    context={
                 
                   cmpny:'cmpny','pcat':pcat,
                   'cprod':cprod,'items':items,
                   'witems':witems
             }
        
    return render(request,'imsuser/userindex.html',context)


def prod_by_cat(request,catid):
    cid=request.session['cid'] 
    procat=ProductCategory.objects.filter(id=catid,cmpid=cid)
    cprod=Product.objects.filter(cmpid=cid,id=catid)
    context={
                  'procat':procat,'cprod':cprod
             }
    return render(request,'imsuser/userindex.html',context)



def viewallprod(request):
    cid = request.session.get('cid')
    cpid = cid
    allprod=Product.objects.filter(cmpid=cpid)
    pcat=ProductCategory.objects.filter(cmpid=cpid)
    context={
                  'cprod':allprod,'pcat':pcat
             }
    return render(request,'imsuser/userindex.html',context)


def prodquickview(request,pid):
    print(pid)
    viewp=Product.objects.get(id=pid)
    print(viewp.cprodname)
    return render(request,'imsuser/prodquickview.html',{'viewp':viewp}) 

#displaying the product details to the customer
def productview(request,prodid):
    userid=request.session['userid']
    cid=request.session['cid'] 
    cmpny=Companies.objects.get(id=cid)
    procat=ProductCategory.objects.filter(id=prodid,cmpid_id=cid)
    pcat=ProductCategory.objects.filter(cmpid_id=cid)
    cprod=Product.objects.get(id=prodid,cmpid_id=cid)
    items = Cart.objects.filter(uid_id=userid)
    qtyofitem=Cart.objects.filter(uid_id=userid).values('id', 'uprodqty')
    witems = WishList.objects.filter(uid_id=userid,status=True)
    grandtotal = items.aggregate(total=Sum(F('uprodqty') * F('prodid__cprodprice')))['total'] or 0
    for item in qtyofitem:
        item_id = item.get('id')
        prodqty = item.get('uprodqty')

    if request.method == 'POST':
            userid=request.session['userid']
            uprodid=prodid
            uprodqty=request.POST['uprodqty']
            if Cart.objects.filter(uid_id=userid, prodid_id=uprodid).exists():
                Cart.objects.filter(id=item_id).update(uprodqty=uprodqty)
                messages.info(request, f'{prodid}Item already exists in the cart.')
                return redirect('productview', prodid=prodid)
            else:
                cartitem = Cart(uprodqty=uprodqty,prodid_id=prodid,uid_id=request.session['userid'],status=True)

                cartitem.save()
                messages.info(request, f'{prodid}Item added to the cart.')
                return redirect('productview',prodid=prodid)
    context={
                  'procat':procat,
                  'cprod':cprod,
                  'pcat':pcat,
                   cmpny:'cmpny',
                  'items': items,
                  'witems': witems,
                  'product_in_cart': Cart.objects.filter(uid_id=userid, prodid_id=prodid).exists(),
                   'grandtotal':grandtotal,
                   'qtyofitem':qtyofitem,
                   'prodqty': prodqty
             }
    return render(request,'imsuser/productview.html',context) 


#Adding item to the cart
def add_to_cart(request,cprdctid):
    userid = request.session['userid']
    if Cart.objects.filter(uid_id=userid, id=cprdctid).exists():
        messages.info(request, f'{cprdctid}Item already exists in the cart.')
        return redirect('usercartview')
    else:
        savetocart =Cart(prodid_id=cprdctid,uid_id=userid,status=True)
        savetocart.save()
        wishlist_item = get_object_or_404(WishList, prodid_id=cprdctid, uid_id=userid)
        wishlist_item.delete()
        print(userid,cprdctid,cprdctid)
        return redirect('userwishlist')
    

#Adding item to the wishlist
def add_to_wishlist(request,wlistid,source_page=None):
    cid = request.session['cid']
    userid = request.session['userid']
    if WishList.objects.filter(uid_id=userid, prodid_id=wlistid).exists():
        pass
    else:
        wlistitem=WishList(prodid_id=wlistid,uid_id=userid,status=True)
        wlistitem.save()
    if source_page == 'userindex':
        return redirect('userindex', cid=cid)
    elif source_page == 'productview':
        return redirect('userwishlist')

    return redirect('userwishlist')


#Removing item from the wishlist
def remove_wlproduct(request,rmvewlid):
        print("hello")
        print(rmvewlid)
        try:
            item = WishList.objects.get(id=rmvewlid)
            item.delete()
            messages.success(request, 'Product removed from Wish List successfully.')
        except Cart.DoesNotExist:
            messages.error(request, 'Product does not exist in Wish List.')
        return redirect('userwishlist')

#Viewing the cart
def usercartview(request):
    cid = request.session['cid'] 
    userid = request.session['userid']
    items = Cart.objects.filter(uid_id=userid)
    witems = WishList.objects.filter(uid_id=userid,status=True)
    pricelist = items.values_list('prodid__cprodprice', flat=True)
    totalprice_sum = items.aggregate(total=Sum('prodid__cprodprice'))['total']
    grandtotal = items.aggregate(total=Sum(F('uprodqty') * F('prodid__cprodprice')))['total'] or 0
    subtotals = []
    for item in items:
        qty=item.uprodqty
        price = item.prodid.cprodprice
        subtotal = qty * price
        subtotals.append(subtotal)
        totalprice_sum += subtotal
    zipped_data = zip(items, subtotals)
    context={
            'items': items,
            'witems': witems,
            'pricelist':pricelist,
            'totalprice_sum':totalprice_sum,
            'subtotals':subtotals,
            'grandtotal':grandtotal,
            'zipped_data': zipped_data,

            
        }
    if request.method == 'POST':
        return redirect('usercartview')
    return render(request, 'imsuser/usercartview.html',context )


from django.db.models import *
#Incrementing and decrementing quantity
def updatecart(request):
    userid = request.session['userid']
    items = Cart.objects.filter(uid_id=userid).values('id', 'uprodqty')
    if request.method == 'POST':
        for item in items:
            item_id = item['id']
            cartqty = request.POST.get(f'cartqty_{item_id}')
            if cartqty is not None and cartqty.isdigit():
                cartqty = int(cartqty)
                Cart.objects.filter(id=item_id).update(uprodqty=cartqty)
                print("h",cartqty)

    return redirect(reverse('usercartview'))

#Remove from cart
def remove_product(request,rmveid):
        print("hello")
        print(rmveid)
        try:
            item = Cart.objects.get(id=rmveid)
            item.delete()
            messages.success(request, 'Product removed from cart successfully.')
        except Cart.DoesNotExist:
            messages.error(request, 'Product does not exist in cart.')
        return redirect('usercartview')


#Wishlist
def userwishlist(request):
    userid = request.session['userid']
    items = Cart.objects.filter(uid_id=userid)
    witems = WishList.objects.filter(uid_id=userid,status=True)
    context={
                'witems':witems,
                'items':items
            }
    return render(request,'imsuser/userwishlist.html',context) 

def usercheckout(request):
    userid=request.session['userid']
    userdet=Customers.objects.get(id=userid)
    cartitems=Cart.objects.filter(uid_id=userid)
    pricelist = cartitems.values_list('prodid__cprodprice', flat=True)
    totalprice_sum = cartitems.aggregate(total=Sum('prodid__cprodprice'))['total']
    grandtotal = cartitems.aggregate(total=Sum(F('uprodqty') * F('prodid__cprodprice')))['total'] or 0
    subtotals = []
    for item in cartitems:
        qty=item.uprodqty
        price = item.prodid.cprodprice
        subtotal = qty * price
        subtotals.append(subtotal)
        totalprice_sum += subtotal
    zipped_data = zip(cartitems, subtotals)
   
    if request.method=='POST':
             newaddress = request.POST['newaddr']
             print(newaddress)
             if newaddress != userdet.uaddr:
                existing_address = NewAddress.objects.filter(uid_id=userid).first()
        
                if existing_address:
                    existing_address.newaddr = newaddress
                    existing_address.save()
                else:
                    updaddr = NewAddress(uid_id=userid, newaddr=newaddress)
                    updaddr.save()

   
    
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(grandtotal)*100  
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id']
    context ={
            'userdet':userdet,
            'cartitems':cartitems,
            'pricelist':pricelist,
            'totalprice_sum':totalprice_sum,
            'subtotals':subtotals,
            'grandtotal':grandtotal,
            'zipped_data': zipped_data,
            'api_key':api_key,
            'order_id':payment_order_id

         }
    return render(request,'imsuser/usercheckout.html',context)

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

from django.utils import timezone
from datetime import *

def billgeneration(request):
    userid=request.session['userid']
    print(userid)
    today = date.today()
    cartitems=Cart.objects.filter(uid=userid,status=False)
    if request.method=='POST':
        order_id = ''.join(random.choice(string.digits) for i in range(4))
        cid = []
        for i in cartitems:
            cid.append(i.id)
            print(i.id)
        print(cid)
        orderdet=Order.objects.create(orderid=order_id,uid_id=userid)
        for c in cid:
            orderdet.cartid.add(Cart.objects.get(id=c))
            Cart.objects.filter(id=c).update(status=True)
            print(c)
        return redirect("billgeneration")
    order_info=Order.objects.filter(uid=userid,orderdate=today)
    context={
        'order_info':order_info
    }
    return render(request,'imsuser/billgeneration.html',context) 





