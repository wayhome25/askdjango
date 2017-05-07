from django.contrib import admin
from .models import GameUser, Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'created_at']
	list_display_links = ['title']

admin.site.register(GameUser)
