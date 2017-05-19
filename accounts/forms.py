from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
	phone_number = forms.CharField()
	address = forms.CharField()

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',) # 단일 튜플은 마지막 콤마 필요

	def save(self):
		user = super().save()

		Profile.objects.create(
			user = user,
			phone_number = self.cleaned_data['phone_number'],
			address = self.cleaned_data['address'])
		return user
