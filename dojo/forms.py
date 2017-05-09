# dojo/forms.py
from django import forms
from .models import Post


''' Form : 직접 필드정의 필요
class PostForm(forms.Form):
	title = forms.CharField(validators=[min_length_3_validator]) # 한줄 문자입력창, 커스텀 validators 옵션 지정 가능
	content = forms.CharField(widget=forms.Textarea) # 여러줄 입력 위젯 설정
'''


class PostForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Post
		fields = ['title', 'content', 'user_agent']
		widgets = {
			'user_agent' : forms.HiddenInput,
		}
		
	''' 내부적으로 구현되어 있음 (멤버변수 인스턴스)
		향후 수정 기능 구현시 활용
	def save(self, commit=True):
		self.instance = Post(**self.cleaned_data)
		if commit:
			self.instance.save()
		return self.instance
	'''
