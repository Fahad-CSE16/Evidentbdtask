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
#LocAL IMPORT
from .models import *
from .forms import *

User = get_user_model()
from django.views.generic import TemplateView




class HomeView(TemplateView):
    template_name='home.html'


def handleSignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Successfulyy Registered')
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'userapp/register.html', {'form': form})


def handleLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="userapp/login.html",
                  context={"form": form})

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')