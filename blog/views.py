from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        Post.objects.create(
            title=title,
            content=content,
            image=image
        )
        return redirect('blog:post_list')
    
    return render(request, 'blog/post_create.html')