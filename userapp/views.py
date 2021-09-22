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
        form = RegisterForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save()
<<<<<<< HEAD
<<<<<<< HEAD
            print("user", user)
            messages.info(request, 'Successfully Registered!')
            login(request, user)
            messages.success(request, f"You are now logged in as {user.email}")
=======
<<<<<<< HEAD
            messages.info(request, 'Successfulyy Registered')
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}")
=======
=======
>>>>>>> 6531267 (custom user working)
            print("user", user)
            messages.info(request, 'Successfully Registered!')
            login(request, user)
            messages.success(request, f"You are now logged in as {user.email}")
<<<<<<< HEAD
>>>>>>> daf0390 (not working)
>>>>>>> 91b7aa5 (resolved)
=======
>>>>>>> 6531267 (custom user working)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'userapp/register.html', {'form': form})


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

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')