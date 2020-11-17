from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    print('register method called')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                 user = User.objects.create_user(
                 username=username,
                 password=password1,
                 email=email,
                 first_name=first_name,
                 last_name=last_name
                 )
                 user.save()
                 print('user created')
                 return redirect('login')
        else:
            messages.info(request,'password doesnot matched')
            return redirect('register')
    else:
        return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')