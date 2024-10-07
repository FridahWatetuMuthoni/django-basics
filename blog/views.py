from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from .forms import PostForm,PostDeleteForm
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts
    }
    return render(request, 'pages/home.html', context)

def blogs(request, tag=None):
    tag_obj = None
    
    if not tag:
        posts = Post.objects.all()
    else:
        tag_obj = get_object_or_404(Tag, slug=tag)
        posts = Post.objects.filter(tags__in=[tag_obj])
    
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'posts':posts,
        'tag':tag_obj
    }
    return render(request, 'blog/blogs.html', context)

def detail(request, slug=None):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'post':post
    }
    return render(request, 'blog/detail.html', context)

@login_required(login_url='account_login')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        context = {
            'form':form
        }
    return render(request, 'blog/create.html',context)

@login_required(login_url='account_login')
def update(request,pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        context = {
            'form':form,
            'post':post
        }
    return render(request, 'blog/update.html', context)

@login_required(login_url='account_login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostDeleteForm(request.POST,instance=post)
        if form.is_valid():
            post.delete()
            return redirect('home')
    else:
        form = PostDeleteForm(instance=post)
        context = {
            'post':post,
            'form':form
        }
        return render(request, 'blog/delete.html',context)