from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import *
from .forms import *
from .decorators import unauthenticated_user
User = get_user_model()
class HomeView(TemplateView):
    template_name='home.html'

@unauthenticated_user
def handleSignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Successfully Registered!')
            login(request, user)
            messages.success(request, f"You are now logged in as {user.email}")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'userapp/register.html', {'form': form})

@unauthenticated_user
def handleLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {user.email}")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request=request, template_name="userapp/login.html")

@login_required(login_url='login')
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')