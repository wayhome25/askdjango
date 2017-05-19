from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',) # 단일 튜플은 마지막 콤마 필요
		
