# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
        'q' : q,
    })


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })
