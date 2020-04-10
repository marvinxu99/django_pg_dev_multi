# posts/views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'posts/home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('posts:home')