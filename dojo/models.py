# dojo/models.py
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField() # DB에 대한 인터페이싱, DB에 저장되는 필드타입
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
