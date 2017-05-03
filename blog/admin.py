from django.contrib import admin
from .models import Post

# 등록법 1 : 기본 ModelAdmin 으로 등록
# admin.site.register(Post)

# 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'content']
#
# admin.site.register(Post, PostAdmin)

# 등록법 3 : 장식자 형태로 지원
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','status', 'created_at', 'tags'] # admin 목록에 보여질 필드 목록
    list_display_links = ['title'] # 목록 내에서 링크로 지정할 필드 목록
    list_editable = ['tags']
    list_per_page = 10 # 디폴트 100
    list_filter = ['created_at']
    actions = ['make_published', 'make_draft', 'make_withdrawn']

    def content_size(self, post): # 함수를 list_display 항목으로 지정 가능
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') # 지정 조건의 다수 Record 를 갱신하고, 그 Record 갯수를 리턴 # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경!'.format(updated_count)) # django message framework 활용
    make_published.short_description = 'Published 로 변경' # 함수의 설명 필드 변경

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') # 지정 조건의 다수 Record 를 갱신하고, 그 Record 갯수를 리턴 # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경!'.format(updated_count)) # django message framework 활용
    make_draft.short_description = 'draft로 변경' # 함수의 설명 필드 변경

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w') # 지정 조건의 다수 Record 를 갱신하고, 그 Record 갯수를 리턴 # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 withdrawn 상태로 변경!'.format(updated_count)) # django message framework 활용
    make_withdrawn.short_description = 'withdrawn 로 변경' # 함수의 설명 필드 변경
