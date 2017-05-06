from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid():
			post = form.save(commit=False) # 중복 save를 방지
			post.ip = request.META['REMOTE_ADDR']
			post.save()
			return redirect('/dojo/')
	else:
		form = PostForm()
	return render(request, 'dojo/post_form.html',{
		'form': form,
	})


def post_edit(request, id):
	post = get_object_or_404(Post, id=id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post) # NOTE: 수정 form은 instance 인자를 추가
		if form.is_valid():
			post = form.save(commit=False) # 중복 save를 방지
			post.ip = request.META['REMOTE_ADDR']
			post.save()
			return redirect('/dojo/')
	else:
		form = PostForm(instance=post)
	return render(request, 'dojo/post_form.html',{
		'form': form,
	})
