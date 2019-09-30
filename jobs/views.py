from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, BadHeaderError
from .forms import ApplicationForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.timezone import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



from .models import Jobs

class JobsList(generic.ListView):
    queryset = Jobs.objects.filter(status=1).order_by('-created_on')
    template_name = 'veritas1/jobs.html'

class JobsDetail(generic.DetailView):
    model = Jobs
    template_name = 'veritas1/jobs_details.html'



# def email(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             from_email = request.POST.get('email')
#             subject = request.POST.get('subject')
#             message =request.POST.get('message')
#             document = request.Files.get('document')
#             email_to =settings.EMAIL_HOST__USER
#             recipient_list = []
#             email = EmailMessage(subject,message,from_email, email_to)
#             base_dir = 'media/documents/'
#             email.attach_file('media/documents/'+str(document))
#             email.send()
#     else:
#         form= ApplicationForm()
#         return render(request, 'veritas1/application.html', {'form':form})


def email(request):
    if request.method == "POST":
        form=ApplicationForm()
        
        form=ApplicationForm(request.POST, request.FILES)

        if form.is_valid:
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = request.POST.get('from_email')
            document = request.FILES.get('document')
            try:
                mail=EmailMessage(subject, message, from_email, ['collinsmusyimi.cm@gmail.com'])
                mail.attach('resume.pdf', document.read(), 'application/pdf')
                mail.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('',  {'message': 'Sent email to %s'%'collinsmusyimi.cm@gmail.com'})
    else:
        form= ApplicationForm()
        return render(request, 'veritas1/application.html', {'form':form})