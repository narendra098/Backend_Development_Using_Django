from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username=request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=name,email=email)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            msgs = 'welcome '+username
            messages.info(request,msgs)
            return redirect('/')
        else:
            messages.info(request,'wrong credentials')
            return redirect('login')
    else:
        return render(request,'login.html')