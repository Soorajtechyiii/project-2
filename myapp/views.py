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
        R= Register(text=text,psw=password,repeatpassword=repeatpassword)
        R.save()
        return HttpResponse('data save')
    else:
        return HttpResponse('not saved')

   

        






    



