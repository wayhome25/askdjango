from django.shortcuts import render, redirect
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
