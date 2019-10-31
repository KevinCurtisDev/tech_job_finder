from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('jobs')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

    

def register(request):
    '''
        This function takes the registration post request variables and checks them against
        custom validations. If the validations pass then a new user is created and the user is taken
        to the login page. Otherwise the user is redirected to the register page with a validation error message.
    '''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                print('That name is already registered')
                messages.error(request, 'That name is already registered')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print ('That email is already registered to a user')
                    messages.error(request, 'That email is already registered to a user')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    print ('You are now registered')
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out')

    return redirect('index')
