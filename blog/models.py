# blgo/models.py
import re
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    title = models.CharField('제목', max_length=100, help_text='제목은 100자 이내로 입력 가능'
        # choices = (
        #     ('제목1', '제목1 레이블'), # (저장될 값, UI에 보여질 레이블)
        #     ('제목2', '제목2 레이블'),
        #     ('제목3', '제목3 레이블'),
        # )
        )
    author = models.CharField(max_length=20)
    content = models.TextField('본문내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator], # form validators 추가 지정 가능
        help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES) # choices filed option을 통해 select 필드로 지정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
