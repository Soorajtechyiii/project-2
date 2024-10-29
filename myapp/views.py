from django.shortcuts import render #type:ignore
from django.template import loader #type:ignore
from django.http import HttpResponse #type:ignore
from myapp.models import Register #type:ignore
def pagehtml(request):
    id=loader.get_template('oopop.html')
    return HttpResponse(id.render())
def getdata(request):
    if request.method =='POST':
        text=request.POST.get('email')
        password=request.POST.get('psw')
        repeatpassword=request.POST.get('psw-repeat')
        R= Register(email=text,psw=password,repeatpassword=repeatpassword)
        R.save()
        if R is not None:
            return render(request,'save.html')
        else:
            return render(request,'oopop.html')
    return HttpResponse('invalid request method')
def save(request):
    id=loader.get_template('save.html')
    return HttpResponse(id.render())
       

        






    



