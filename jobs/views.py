from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .forms import ApplicationForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.timezone import timezone
from django.shortcuts import render


from .models import Jobs

class JobsList(generic.ListView):
    queryset = Jobs.objects.filter(status=1).order_by('-created_on')
    template_name = 'veritas1/jobs.html'

class JobsDetail(generic.DetailView):
    model = Jobs
    template_name = 'veritas1/jobs_details.html'



def email(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message =request.POST.get('message')
            document = request.POST.get('document')
            email_from =settings.EMAIL_HOST__USER
            recipient_list = [email]
            email = EmailMessage(subject,message,email_from, recipient_list)
            base_dir = 'media/documents/'
            email.attach_file('media/documents/'+str(document))
            email.send()
    else:
        form= ApplicationForm()
        return render(request, 'veritas1/application.html', {'form':form})


