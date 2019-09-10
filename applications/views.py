from django.core.mail import send_mail, BadHeaderError, EmailMessage,EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            attach = request.FILES['attach']
            try:
                msg=EmailMessage(subject, message, from_email, ['admin@example.com'])
                msg.attach(attach.name, attach.read(), attach.content_type)
                msg.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "veritas1/upload.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')