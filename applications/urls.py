from django.urls import path,include
from .views import model_form_upload

urlpatterns = [
    path('applications/', model_form_upload, name='applications')
]
