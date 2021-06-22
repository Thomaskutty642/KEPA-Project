from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User,auth
#from django.contrib.auth import authenticate,login
from django.contrib import messages
#from .models import USer
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('password')
        print(pas)
        user = auth.authenticate(username=username, password=pas)
        print(user)
        if user is not None :
            auth.login(request,user)
            messages.info(request, ('You Have Been Logged In!'))
            return redirect('/')
        else :
            messages.info(request, ('Invalid credentials'))
            return render(request, 'login.html')
        
    else:
	    return render(request, 'login.html')










def register(request):

    if (request.method == 'POST'):
        print(request.POST)
        print("post invoked")
        first_name = request.POST.get ('first_name')
        last_name = request.POST.get ('last_name')
        username = request.POST.get ('username')
        email = request.POST.get ('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get ('password2')
        print(first_name,last_name,username,password1,password2,email)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username not availabe')
                print ('Username not availabe')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Account already exist with this mail id')
                print('Account already exist')
                return redirect ('register')
            else :
                user= User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name);
                user.save()
                print('USER CREATED')
                return render(request,'login.html')

        else:
            messages.info(request,'Password not matching')
            print('Password not matching')
            return render(request,'register.html')

        ##return render(request,'register.html') 
    
    else :
        return render(request,'register.html')




def logout_user (request):
    auth.logout(request)
    return redirect('/')