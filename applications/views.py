from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            files = request.FILES.getlist('attach')
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, files, from_email, ['admin@example.com'])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()


            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "veritas1/upload.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')