from django.shortcuts import render ,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def frontpage(request):
    return render(request, 'frontpage.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Already Existe')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user .save();
        else:
            messages.info(request,'The confirm password dosn\'t much')                
                
                
    
    return render(request, 'signup.html')




def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('front')
        else:
            messages.info(request,'this account does not exist')
    return render(request, 'login.html') 


def logout(request):
    auth.logout(request)
    return redirect('front')