from django.shortcuts import render
from django.db.models import Q
#basic import
from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.views.generic import View
import time
#Userlogin signup, import
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash,get_user_model
from django.contrib.auth.views import PasswordChangeForm, PasswordResetCompleteView,\
     PasswordResetConfirmView, PasswordResetView,PasswordResetForm,PasswordResetDoneView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
#LocAL IMPORT
from .models import *
from .forms import *
from .decorators import unauthenticated_user
User = get_user_model()
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name='home.html'

@unauthenticated_user
def handleSignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            print("calling")
            user = form.save()
            print("user", user)
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
        email =request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(username=email, password=password)
        print("user", user)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {user.email}")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request=request,
                  template_name="userapp/login.html",)
@login_required(login_url='login')
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')