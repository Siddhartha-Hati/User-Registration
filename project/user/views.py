from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,LoginForm

# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password')
            pass2 = form.cleaned_data.get('c_password')
            # img=form.cleaned_data.get("p_image")

            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not the same.")
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username  or password is incorrect")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')