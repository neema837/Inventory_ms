from django.shortcuts import *
from.models import*
from django.contrib import messages
from datetime import datetime
def supplogin(request):
   if request.method=='POST':
      try:
         spmail=request.POST['spmail']
         sppwd=request.POST['sppwd']
         check=Suppliers.objects.get(spmail=spmail,sppwd=sppwd)
         request.session['id']=check.id
         request.session['spmail']=check.spmail
         request.session['sppwd']=check.sppwd
         return redirect('supphome')
      except Suppliers.DoesNotExist as e:
         messages.info(request,"Invalid Credentials")
   return render(request,'supplier/supplogin.html')
def suppreg(request):
   if request.method=='POST':
         spname=request.POST['spname']
         spmail=request.POST['spmail']
         spphno=request.POST['spphno']
         spaddr=request.POST['spaddr']
         spcity=request.POST['spcity']
         spstate=request.POST['spstate']
         spzip=request.POST['spzip']
         spcountry=request.POST['spcountry']
         splic=request.FILES.get('splic')
         if Suppliers.objects.filter(spmail=spmail).exists():
            messages.info(request,'This email already exists')
         else:
            saveval=Suppliers(spname=spname,spmail=spmail,spphno=spphno,
                              spaddr=spaddr,spcity=spcity,spstate=spstate,
                              spzip=spzip,spcountry=spcountry,splic=splic)
            saveval.save()
   return render(request,'supplier/suppreg.html')
def supphome(request):
   return render(request,'supplier/supphome.html')
def saddprod(request):
      sid= request.session['id']
      spcat=SproductCategory.objects.filter(supid=sid)
      if request.method=='POST':
        sprodname=request.POST['sprodname']
        sproddesc=request.POST['sproddesc']
        sprodbrand=request.POST['sprodbrand']
        sprodprice=request.POST['sprodprice']
        sprodminqty=request.POST['sprodminqty']
        sprodmaxqty=request.POST['sprodmaxqty']
        sprodstock=request.POST['sprodstock']
        sprodimage=request.FILES.get('sprodimage')
        spaddingdate=datetime.now().date()
        spexpdate=request.POST['cpexpdate']
        sprodsppid=request.POST['sprodcatgry']
        saveval=Sproduct(sprodname=sprodname,sproddesc=sproddesc,
                        sprodbrand=sprodbrand,sprodprice=sprodprice,sprodminqty=sprodminqty,
                        sprodmaxqty=sprodmaxqty,sprodstock=sprodstock,sprodimage=sprodimage,
                        sprodcat_id=sprodsppid,spaddingdate=spaddingdate,spexpdate=spexpdate)
        saveval.save()
        return redirect('saddprod')   
      return render(request,'supplier/saddprod.html',{'spcat':spcat})
def sviewprod(request):
        sprod=Sproduct.objects.all()
        context={
            'sprod':sprod
        }
        return render(request,'supplier/sviewprod.html',context)
def sviewoneprod(request,spid):
        sprodid=Sproduct.objects.get(id=spid)
        return render(request,'supplier/sviewoneprod.html',{'sprodid':sprodid})
def supdateprod(request,upid):
     sprodid=Sproduct.objects.get(id=upid)
     sprodid.spcat=SproductCategory.objects.all()
     if request.method=='POST':
        sprodid.sprodname=request.POST['sprodname']
        sprodid.sproddesc=request.POST['sproddesc']
        sprodid.sprodbrand=request.POST['sprodbrand']
        sprodid.sprodprice=request.POST['sprodprice']
        sprodid.sprodminqty=request.POST['sprodminqty']
        sprodid.sprodmaxqty=request.POST['sprodmaxqty']
        sprodid.sprodstock=request.POST['sprodstock']
        sprodimage=request.FILES.get('sprodimage')
        if sprodimage:
            sprodid.sprodimage=sprodimage
            sprodid.save()
        sprodid.save()
        return redirect('sviewprod')
     return render(request,'supplier/supdateprod.html',{'sprodid':sprodid}) 
def sdeleteprod(request,dpid):
    sprodid=Sproduct.objects.get(id=dpid)
    if request.method=='POST':
        sprodid.delete()
        return redirect("sviewprod")
    return render(request,"supplier/sviewprod.html",{'sprodid':sprodid})
def saddcat(request):
   if request.method=='POST':
        catname=request.POST['catname']
        spname=request.session['id']
        saveval=SproductCategory(catname=catname,supid_id=spname)
        saveval.save()
        return redirect('saddprod')
   return render(request,'supplier/saddprod.html')
