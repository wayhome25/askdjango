# mysite/urls.py

from django.conf import settings
from django.conf.urls import include, url
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

# django-debug-toolbar 세팅
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#     url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
