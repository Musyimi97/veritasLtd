from django.urls import path,include
from jobs.views import JobsDetail, JobsList


urlpatterns = [
    path('jobs',JobsList.as_view(),name='jobs' ),
    path('<slug:slug>/', JobsDetail.as_view(), name='jobs_detail'),

]
