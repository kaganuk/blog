from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required


def post_list(request):
    """A list page for posts."""
    posts = Post.objects.posts()
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_new(request):
    """A page for create new posts."""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    """A page for post details."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_edit(request, pk):
    """A page for edit posts."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
