# blgo/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField('제목', max_length=100, help_text='제목은 100자 이내로 입력 가능'
        # choices = (
        #     ('제목1', '제목1 레이블'), # (저장될 값, UI에 보여질 레이블)
        #     ('제목2', '제목2 레이블'),
        #     ('제목3', '제목3 레이블'),
        # )
        )
    content = models.TextField('본문내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
