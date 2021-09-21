from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('login/',handleLogin,name='login'),
    path('logout/',handleLogout,name='logout'),
    path('register/',handleSignup,name='register'),
]
