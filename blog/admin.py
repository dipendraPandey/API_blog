from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'date_published', 'author']


admin.site.register(BlogPost)