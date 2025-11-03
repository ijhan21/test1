from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                image=image
            )
            messages.success(request, '✅ 글이 작성되었습니다!')
            return redirect('blog:post_list')
        else:
            messages.error(request, '❌ 제목과 내용을 입력해주세요.')
    
    return render(request, 'blog/post_create.html')