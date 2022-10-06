from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    context = {"posts": all_posts}
    return render(request, 'posts/index.html', context)


def getPost(request, pk):
    selected_post = Post.objects.get(id=pk)

    context = {"post": selected_post}
    return render(request, 'posts/details.html', context)


def newPost(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': PostForm, 'button_text': 'Create'}
    return render(request, 'posts/new_edit.html', context)


def editPost(request, pk):
    selected_post = Post.objects.get(id=pk)
    form = PostForm(instance=selected_post)

    if request.POST:
        form = PostForm(request.POST, instance=selected_post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form, 'button_text': 'Edit'}
    return render(request, 'posts/new_edit.html', context)

def deletePost(request, pk):
    selected_post = Post.objects.get(id=pk)
    selected_post.delete()

    return redirect('home')