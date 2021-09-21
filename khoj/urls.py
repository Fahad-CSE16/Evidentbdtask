from django.urls import path
from .views import *
urlpatterns = [
    path('',khoj_the_search,name='khoj_the_search'),
]
