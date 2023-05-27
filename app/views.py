from django.shortcuts import *
from django.http import HttpResponse
from.models import*
from django.contrib import*

# Create your views here.
def index(request):
   #return HttpResponse("hello")
   return render(request,'index.html')
def signin(request):
   #return HttpResponse("")
   #return redirect('/')
    #path('signin',views.signin,name="signin"),
   return render(request,'signin.html')
def reg(request):
   return render(request,'reg.html')
def home(request):
   return render(request,'home.html')


#def reg(request):
#    if request.method=='POST':
       # name=request.POST['firstname']
       # email=request.POST['email']
       # pwd=request.POST['pass']
       # cpwd=request.POST['repass']
        #if pwd==cpwd:
        #    if Registeration.objects.filter(email=email).exists():
         #       messages.info(request,'email exists')
         #   else:
          #       saveval=Registeration(name=name,email=email,password=pwd)
             #    saveval.save()
             #    return redirect('login')
       # else:
            #    messages.info(request,'password doesnt match')

#    return render(request,'reg.html')
