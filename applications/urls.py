from django.urls import path,include
from applications import views
urlpatterns = [
    path('', views.upload, name='resume')
]
