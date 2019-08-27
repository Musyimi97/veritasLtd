from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Applications
# Create your views here.


def model_form_upload(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ApplicationForm()
    return render(request, 'veritas1/upload.html', {
        'form': form
    })