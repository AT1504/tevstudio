# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from .views import index, successView

urlpatterns = [
    path('', index, name='index'),
    path('success/', successView, name='success'),
]