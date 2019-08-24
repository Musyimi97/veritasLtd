from django.views import generic
from .models import Jobs

class JobsList(generic.ListView):
    queryset = Jobs.objects.filter(status=1).order_by('-created_on')
    template_name = 'veritas1/jobs.html'

class JobsDetail(generic.DetailView):
    model = Jobs
    template_name = 'veritas1/jobs_details.html'
