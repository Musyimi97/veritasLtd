from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'veritas1/events.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'veritas1/single.html'