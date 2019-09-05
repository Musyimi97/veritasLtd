from django.urls import path,include
from .views import emailView, successView
urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success')
]
