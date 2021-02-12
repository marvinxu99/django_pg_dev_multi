# posts/views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .forms import PostForm
from .models import Post


class AllPostsListView(ListView):
    model = Post
    template_name = 'posts/all_posts.html'
    paginate_by = 4


class AllPostsByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing posts created by current user."""
    model = Post
    template_name = 'posts/all_posts.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user).order_by('created_at')


# class CreatePostView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'posts/create_post.html'
#     success_url = reverse_lazy('posts:all_posts')
@login_required()
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post()

            new_post.title = form.cleaned_data['title']
            new_post.cover = form.cleaned_data['cover']
            new_post.created_by = request.user
            new_post.created_at = timezone.now()
            new_post.save()

            return redirect('posts:all_posts')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', { 'form': form })


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.created_by == request.user:
        post.delete()

    return redirect('posts:all_posts')


def responsive_cards(request):
    return render(request, 'posts/responsive_cards.html')


class AllPostsCarouselView(ListView):
    model = Post
    template_name = 'posts/all_posts_carousel.html'
#    template_name = 'posts/carousel_demo.html'

def carousel_demo(request):
    return render(request, 'posts/carousel_demo.html')
