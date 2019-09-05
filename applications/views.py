from django.shortcuts import render,redirect
from .forms import ResumeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def emailView(request):
    if request.method == 'GET':
            form = ResumeForm()
    else:
        form = ResumeForm(request.POST)
        if form.is_valid():
            experience = form.cleaned_data['experience']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            attach = request.FILES['attach']
            try:
                send_mail(experience, message, from_email, attach,  ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
   return HttpResponse('Success! Thank you for your message.')



    