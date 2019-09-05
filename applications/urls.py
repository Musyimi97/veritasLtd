from django.urls import path,include
from .views import emailView, successView
urlpatterns = [
    path('email/', emailView, name='resume'),
    path('success/', successView, name='success')
]
