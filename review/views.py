from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

def post_list(request):
    # 생성일(created_date)기준으로 정렬
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'review/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'review/post_detail.html', {'post': post})

@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('review:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'review/post_edit.html', {'form': form})

@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('review:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'review/post_edit.html', {'form': form})

@login_required()
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('review:index')

class PostLV(ListView):
    model = Post
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    template_name = 'review/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5


