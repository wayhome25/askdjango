from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid(): # form의 모든 validators 호출 유효성 검증 수행
			# 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
			# 검증에 실패시 form.error 에 오류 정보를 저장
			'''
			# 저장방법1) - 가장 일반적인 방법
			post = Post()
			post.title = form.cleaned_data['title']
			post.content = form.cleaned_data['content']
			post.save()

			# 저장방법2)
			post = Post(title = form.cleaned_data['title'],
						content = form.cleaned_data['content'])
			post.save()

			# 저장방법3)
			post = Post.objects.create(title = form.cleaned_data['title'],
										content = form.cleaned_data['content'])
			'''
			# 저장방법4)
			pott = Post.objects.create(**form.cleaned_data) # unpack 을 통해 방법3과 같이 저장

			return redirect('/dojo/') # namespace:name
	else:
		form = PostForm()
	return render(request, 'dojo/post_form.html',{
		'form': form,
	})
