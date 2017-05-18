# blgo/models.py
import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
	if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
		raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
	STATUS_CHOICES = (  # NOTE: choices 필드옵션 적용시 사용
	    ('d', 'Draft'),
	    ('p', 'Published'),
	    ('w', 'Withdrawn'),
	)
	title = models.CharField('제목', max_length=100, help_text='제목은 100자 이내로 입력 가능')
                         # choices = (
                         #     ('제목1', '제목1 레이블'), # (저장될 값, UI에 보여질 레이블)
                         #     ('제목2', '제목2 레이블'),
                         #     ('제목3', '제목3 레이블'),
                         # )

	author = models.ForeignKey(settings.AUTH_USER_MODEL) # NOTE: 내장 User Model ForeignKey 적용
	content = models.TextField('본문내용')

	# photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d') # 업로드 경로 지정 (파일이 업로드 될 때 해당 값 참고, 기존 파일에는 영향 x)
	photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
								processors=[Thumbnail(300,300)],
								format='JPEG',
								options={'quality': 50} )
	# photo_thumbnail = ImageSpecField(source='photo',
	# 								processors=[Thumbnail(300,300)],
	# 								format='JPEG',
	# 								options={'quality': 60}
	# 								)

	tags = models.CharField(max_length=100, blank=True)
	lnglat = models.CharField(max_length=50, blank=True,
	                          # form validators 추가 지정 가능
	                          help_text='경도/위도 포맷으로 입력',
							  validators=[lnglat_validator])
	# choices filed option을 통해 select 필드로 지정
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	tag_set = models.ManyToManyField('Tag', blank=True)  # 문자열로도 지정 가능 (순서 상관 x)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self): # 강추! 별 50개!!
		return reverse('blog:post_detail', args=[self.id])

	class Meta:
		ordering = ['-id']  # 모델정렬기준 : 해당필드 (id) 기준 내림차순 정렬

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=20)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name
