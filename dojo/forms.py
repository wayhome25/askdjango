# dojo/forms.py
from django import forms

def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')


class PostForm(forms.Form):
	title = forms.CharField(validators=[min_length_3_validator]) # 한줄 문자입력창, 커스텀 validators 옵션 지정 가능
	content = forms.CharField(widget=forms.Textarea) # 여러줄 입력 위젯 설정
