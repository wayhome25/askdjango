# mysite/urls.py

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
# from django.views.generic import RedirectView
# from blog import views


urlpatterns = [
    # url(r'^$', views.post_list),
    # url(r'^$', RedirectView.as_view(pattern_name='blog:post_list')),
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
	url(r'^dojo/', include('dojo.urls', namespace='dojo')),
]

# media 파일 서빙을 위한 설정 - static files와는 다르게 개발서버에서 서빙 미지원, 개발 편의성 목적으로 직접 서빙 Rule 추가
# 단, settings.DEBUG = False일때는 static 함수에서 빈 리스트를 리턴
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django-debug-toolbar 세팅
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#     url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
