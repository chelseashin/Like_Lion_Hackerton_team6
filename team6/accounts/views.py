from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def signup(request):
    auth_mode = 'signup'    
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password1'):
            user = User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))

            profile = Profile()
            profile.nickname = request.POST.get('nickname')
            profile.email = request.POST.get('email')
            profile.user = user
            profile.save()

            auth.login(request, user)
            return redirect('index')
    return render(request, 'accounts/auth_form.html', {'auth_mode': auth_mode})

    
def login(request):
    auth_mode = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'accounts/auth_form.html', {'error' : 'username or password is incorrect!'})
    return render(request, 'accounts/auth_form.html', {'auth_mode': auth_mode})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'accounts/signup.html')