from django.urls import path
from .views import *
from .api import *
urlpatterns = [
    path('',khoj_the_search,name='khoj_the_search'),
    path('api/',ResultsListView.as_view(),name='khoj_the_search'),
]
