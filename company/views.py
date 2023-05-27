from django.shortcuts import *
from.models import*
from employee.models import*
from django.contrib import messages
import random,string
from IMS.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
def comlogin(request):
    if request.method=='POST':
      try:
         cpmail=request.POST['cpmail']
         cppwd=request.POST['cppwd']
         check=Companies.objects.get(cpmail=cpmail,cppwd=cppwd)
         request.session['id']=check.id
         request.session['cpmail']=check.cpmail
         request.session['cppwd']=check.cppwd
         return redirect('comhome')
      except Companies.DoesNotExist as e:
         messages.info(request,"Invalid Credentials")
    return render(request,'company/comlogin.html')
def comreg(request):
    if request.method=='POST':
        cpname=request.POST['cpname']
        cpmail=request.POST['cpmail']
        cpphno=request.POST['cpphno']
        cpaddr=request.POST['cpaddr']
        cpcity=request.POST['cpcity']
        cpzip=request.POST['cpzip']
        cpstate=request.POST['cpstate']
        cpcountry=request.POST['cpcountry']
        cptype=request.POST['cptype']
        cplic=request.FILES.get('cplic')
        cplogo=request.FILES.get('cplogo')
        if Companies.objects.filter(cpmail=cpmail).exists():
            messages.info(request,'This email is already existing')
        else:
            saveval=Companies(cpname=cpname,cpmail=cpmail,cpphno=cpphno,
                              cpaddr=cpaddr,cpcity=cpcity,cpzip=cpzip,
                              cpstate=cpstate,cpcountry=cpcountry,cptype=cptype,
                              cplic=cplic,cplogo=cplogo)
            saveval.save()
    return render(request,'company/comreg.html')
def comhome(request):
   return render(request,'company/comhome.html')
def caddemploy(request):
   if request.method=='POST':
      cmpid=request.session['id']
      empname=request.POST['empname']
      empmail=request.POST['empmail']
      empphone=request.POST['empphone']
      if Employdata.objects.filter(empmail=empmail).exists():
         messages.info(request,'This email is already existing')
      else:
         saveval=Employdata(empname=empname,empmail=empmail,empphone=empphone,cmpid_id=cmpid)
         saveval.save()
        # print(saveval.id)
         request.session['empid'] = saveval.id
         request.session['empmail'] = saveval.empmail
         request.session['empname'] = saveval.empname

         return redirect('send_empmail',eid=request.session['empid'])
   return render(request,'company/caddemploy.html')

def send_empmail(request,eid):
      emp=Employdata.objects.get(id=eid)
      if request.method=='POST':
          mail=request.POST['empmail']
          name=request.POST['empname']
          subject='Hi,' +format(name)
          recepient=str(mail)

          characters = string.ascii_letters + string.digits +string.punctuation
          password = ''.join(random.choice(characters) for i in range(8))
          Employdata.objects.filter(id=eid).update(emppwd=password)

          message='''Welcome new employee . Please use your 
                  emailid and the given password" +format(password)"to login to the system'''
          send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
      return render(request,'company/send_empmail.html',{'emp':emp})








 
        

