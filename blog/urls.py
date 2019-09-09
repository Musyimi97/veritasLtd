from django.urls import path,include
from blog.views import PostDetail, PostList

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
