from django.http import JsonResponse
from django.shortcuts import *
from.models import*
from django.contrib import messages
from datetime import datetime,date
import random,string
from supplier.models import *
from company.models import *



def employlogin(request):
      if request.method=='POST':
            try:
               empmail=request.POST['empmail']
               emppwd=request.POST['emppwd']
               check=Employdata.objects.get(empmail=empmail,emppwd=emppwd)
               request.session['empid']=check.id
               request.session['empmail']=check.empmail
               request.session['emppwd']=check.emppwd
               des=Employdata.objects.get(id=check.id)
               print(des.designation)
               print(empmail,emppwd)
               if des.designation=='supervisor':
                    return redirect('supervisorhome')
               elif des.designation=='purchasing officer':
                    return redirect('emphome')
            except Employdata.DoesNotExist as e:
               messages.info(request,"Invalid Credentials")
      return render(request,'employee/employlogin.html')


def employreg(request):
   return render(request,'employee/employreg.html')


def emphome(request):
   return render(request,'employee/emphome.html')

def supervisorhome(request):
   return render(request,'employee/supervisorhome.html')

def supervisoraddtask(request):
    pid = request.session['empid']
    empid = Employdata.objects.get(id=pid)
    cmpid = empid.cmpid_id
    empdata=Employdata.objects.filter(cmpid=cmpid)
    context={
        'empdata':empdata
    }
    if request.method=='POST':
      employid=request.POST.get('empid')
      taskname=request.POST['taskname']
      taskdesc=request.POST['taskdesc']
      duedate=request.POST['duedate']
      timedur=request.POST['timedur']
      saveval=Tasks(taskname=taskname,taskdesc=taskdesc,
                    duedate=duedate,timeofcomp=timedur,
                    empid_id=employid,cmpid_id=cmpid,status=True)
      saveval.save()
    return render(request,'employee/supervisoraddtask.html',context)

def supervisorviewtask(request):
    pid = request.session['empid']
    empid = Employdata.objects.get(id=pid)
    cmpid = empid.cmpid_id
    taskdata=Tasks.objects.filter(cmpid=cmpid)
    context={
            'taskdata':taskdata
    }
    return render(request,'employee/supervisorviewtask.html',context)

def eaddprod(request):
   pid = request.session['empid']
   empid = Employdata.objects.get(id=pid)
   cpid = empid.cmpid_id
   pcat=ProductCategory.objects.filter(cmpid=cpid)
   if request.method=='POST':
        cprodname=request.POST['cprodname']
        cproddesc=request.POST['cproddesc']
        cprodbrand=request.POST['cprodbrand']
        cprodprice=request.POST['cprodprice']
        cprodminqty=request.POST['cprodminqty']
        cprodmaxqty=request.POST['cprodmaxqty']
        cprodstock=request.POST['cprodstock']
        cprodimage=request.FILES.get('cprodimage')
        cpaddingdate=datetime.now().date()
        cpexpdate=request.POST['cpexpdate']
        cprodsppid=request.POST['cprodcatgry']
        saveval=Product(cprodname=cprodname,cproddesc=cproddesc,
                        cprodbrand=cprodbrand,cprodprice=cprodprice,cprodminqty=cprodminqty,
                        cprodmaxqty=cprodmaxqty,cprodstock=cprodstock,cprodimage=cprodimage,
                        cprodcat_id=cprodsppid,cpaddingdate=cpaddingdate,cpexpdate=cpexpdate,cmpid_id=cpid)
        saveval.save()
        return redirect('eaddprod')   
   return render(request,'employee/eaddprod.html',{'pcat':pcat})


def eviewprod(request):
        allprod=Product.objects.all()
        pid = request.session['empid']
        empid = Employdata.objects.get()
        cpid = empid.cmpid
        pcat=ProductCategory.objects.filter(cmpid=cpid)
        cprod=Product.objects.all()
        context={
            'cprod':cprod,'pcat':pcat,'allprod':allprod
        }
        return render(request,'employee/eviewprod.html',context)

def eprod_by_cat(request,cid):
     prodbycat=Product.objects.filter(cprodcat=cid)
     empid = Employdata.objects.get()
     cpid = empid.cmpid
     pcat=ProductCategory.objects.filter(cmpid=cpid)
     context={
                  'cprod':prodbycat,'pcat':pcat
             }
     return render(request,'employee/eviewprod.html',context)


def eviewoneprod(request,pid):
        prodid=Product.objects.get(id=pid)
        return render(request,'employee/eviewoneprod.html',{'prodid':prodid})


def eupdateprod(request,pid):
     prodid=Product.objects.get(id=pid)
     prodid.pcat=ProductCategory.objects.all()
     if request.method=='POST':
        prodid.cprodname=request.POST['cprodname']
        prodid.cproddesc=request.POST['cproddesc']
        prodid.cprodbrand=request.POST['cprodbrand']
        prodid.cprodprice=request.POST['cprodprice']
        prodid.cprodminqty=request.POST['cprodminqty']
        prodid.cprodmaxqty=request.POST['cprodmaxqty']
        prodid.cprodstock=request.POST['cprodstock']
        cprodimage=request.FILES.get('cprodimage')
        if cprodimage:
            prodid.cprodimage=cprodimage
            prodid.save()
        prodid.save()
        return redirect('eviewprod')
     return render(request,'employee/eupdateprod.html',{'prodid':prodid}) 

def edeleteprod(request,did):
    prodid=Product.objects.get(id=did)
    if request.method=='POST':
        prodid.delete()
        return redirect("eviewprod")
    return render(request,"employee/eviewprod.html",{'prodid':prodid})


#modal function 
def addcat(request):
   if request.method=='POST':
        pid = request.session['empid']
        empid = Employdata.objects.get(id=pid)
        cpid = empid.cmpid_id
        catname=request.POST['catname']
        catimage=request.FILES.get('catimage')
        saveval=ProductCategory(catname=catname,cmpid_id=cpid,catimage=catimage)
        saveval.save()
        return redirect('eaddprod')
   return render(request,'employee/eaddprod.html')


#Suppliers
def eviewsupp(request):
    suppinfo=Suppliers.objects.all()
    context={
        'suppinfo':suppinfo
    }
    return render(request,'employee/eviewsupp.html',context)


def eviewspproducts(request,spid):
    spproducts = Sproduct.objects.filter(supid=spid)
    request.session['sid']= spid
    spcat=SproductCategory.objects.filter(supid=spid)
    sprod=Sproduct.objects.filter(supid=spid)
    context={
                 'spproducts':spproducts,
                 'spcat':spcat,
                 'sprod':sprod,
                 'spid':spid,


    }
    return render(request,'employee/eviewspproducts.html',context)


def esplrprod_by_cat(request,catid):
     print(catid)
     print("hello")
     sid=request.session['sid']
     print(sid)
     sprod=Sproduct.objects.filter(sprodcat=catid,supid=sid)
     spcat=SproductCategory.objects.filter(supid=sid)
     context={
                  'sprod':sprod,
                  'spcat':spcat,
                  'sid':sid
             }     
     return render(request,'company/viewspproducts.html',context)

def purchases(request):
    return render(request,'employee/purchases.html')

def createrfq(request,spid):
    pid = request.session['empid']
    empid = Employdata.objects.get(id=pid)
    cmpid = empid.cmpid_id
    current_date = date.today()
    formatted_date = current_date.strftime('%Y-%m-%d')
    purchase_no=''.join(random.choice(string.digits) for i in range(4))
    products=Sproduct.objects.filter(supid=spid)
    suppinfo=Suppliers.objects.get(id=spid)
    context={
        'suppinfo':suppinfo,
        'purchase_no':purchase_no,
        'current_date':formatted_date,
        'products':products,

    }
    if request.method=='POST':
        product_id = request.POST.get('type')
        productdet=Sproduct.objects.get(id=product_id)
        purchaseqty = request.POST['purchaseqty']
        totalprice=int(purchaseqty) * float(productdet.sprodprice)

        saveval=Cpurchase(purchaseno=purchase_no,supid_id=spid,
                          prodid_id=product_id,cmpid_id=cmpid,purchaseqty=purchaseqty,totalprice=totalprice)
        saveval.save()
    return render(request,'employee/purchasepayment.html',context)


def get_product_price(request):
    product_id = request.GET.get('product_id')
    product = Sproduct.objects.get(id=product_id)
    product_price = product.sprodprice

    response_data = {
        'product_price': product_price
    }
    return JsonResponse(response_data)


def emp_logout(request):
    del request.session['empid']
    return redirect('index')

def purchasepayment(request,orderid):
    return render(request,'employee/purchasepayment.html')


