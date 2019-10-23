from django.views import generic
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'veritas1/events.html'
    model =Post
    paginate_by=4

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'veritas1/single.html'