# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

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


def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save()
			return redirect(post) # post.get_absolute_url() => post detail
	else:
		form = PostForm()
	return render(request, 'blog/post_form.html', {
		'form': form,
	})


def post_edit(request, id):
	post = get_object_or_404(Post, id=id)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(post)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_form.html', {
		'form': form,
	})
