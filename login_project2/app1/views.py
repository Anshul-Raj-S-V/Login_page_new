from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Home Page
@login_required(login_url ='login')
def HomePage(request):
    return render(request, 'home.html')

# Signup Function
def Signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')

        # Fix: Correct user creation method
        my_user = User.objects.create_user(username=uname, password=password)
        my_user.save()
        print(f"User Created: {uname}")  # Debugging print
        return redirect('login')  

    return render(request, 'signup.html')

# Login Function
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)  # This should now print correctly

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")  # Better error message

    return render(request, 'login.html')
