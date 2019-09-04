from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Applications
from django.core.files.storage import FileSystemStorage
# Create your views here.



def upload (request):
    context = {}
    if request.method == 'POST':
        uploaded_file=request.FILES['document']
        fs = FileSystemStorage()
        name= fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render (request, 'veritas1/upload.html', context)


def upload_book(request):
    if request.method =='POST':
        form=ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            form=ApplicationForm()
    return render(request, 'veritas1/upload.html',{
        'form':form
    })
    