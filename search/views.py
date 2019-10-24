from django.shortcuts import render
from django.db.models import Q
from jobs.models import Jobs
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Jobs.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'veritas1/search.html', context)

        else:
            return render(request, 'veritas1/search.html')

    else:
        return render(request, 'veritas1/search.html')