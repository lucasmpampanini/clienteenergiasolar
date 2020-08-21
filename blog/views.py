from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(DetailView):
    queryset = Post.objects.all()
    template_name = 'post_details.html'