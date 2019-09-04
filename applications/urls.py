from django.urls import path,include
from .views import model_form_upload, upload

urlpatterns = [
    path('resume/application/', views.upload, name='resume')
]
