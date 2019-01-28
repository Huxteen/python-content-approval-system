from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.


# Process and redirect signup form data 
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            if request.POST['password'] == request.POST['cpassword']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    messages.error(request, 'Username has already been taken')
                    return render(request, 'accounts/signup.html')
                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
                    auth.login(request, user)
                    return redirect('/')
            else:
                messages.error(request, 'Password must match')
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html')


# Process and redirect login form data
def login(request): 
    if request.user.is_authenticated:
        return redirect('/')
    else: 
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or password do not match our record')
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/login.html')


# The logout function kills all active session
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

