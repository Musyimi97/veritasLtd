# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [

    path('email/', emailView, name='contact'),
    path('success/', successView, name='success'),
]