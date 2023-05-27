from django.shortcuts import *
from.models import*
from django.contrib import messages
from datetime import datetime
def employlogin(request):
      if request.method=='POST':
            try:
               empmail=request.POST['empmail']
               emppwd=request.POST['emppwd']
               check=Employdata.objects.get(empmail=empmail,emppwd=emppwd)
               request.session['empid']=check.id
               request.session['empmail']=check.empmail
               request.session['emppwd']=check.emppwd
               print(empmail,emppwd)
               return redirect('emphome')
            except Employdata.DoesNotExist as e:
               messages.info(request,"Invalid Credentials")
      return render(request,'employee/employlogin.html')


def employreg(request):
   return render(request,'employee/employreg.html')


def emphome(request):
   return render(request,'employee/emphome.html')


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

def prod_by_cat(request,cid):
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

def emp_logout(request):
    del request.session['empid']
    return redirect('index')

