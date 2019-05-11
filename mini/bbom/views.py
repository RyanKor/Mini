from django.shortcuts import render, redirect
from .forms import PostForms, CommentForms, UserForms
from .models import Post, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts':posts })

@login_required(login_url='/accounts/login/')
def new(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForms()
        return render(request, 'new.html', { 'form':form })

@login_required(login_url='/accounts/login/')
def edit(request, post_pk):
    post = Post.objects.get(post_pk=post.pk)
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()
        return redirect('detail', post.pk)
    else:
        form = PostForms(instance = post)
        return render(request, 'edit.html', { 'form':form })
    
def delete(request, post_pk):
    post = Post.objects.get(post_pk=post.pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForms()
            error = "이미 존재하는 아이디입니다"
            return render(request, 'registration/signup.html', {'form':form, 'error':error})
    else:
        form = UserForms()
        return render(request, 'registration/signup.html', {'form': form})
