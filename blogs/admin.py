from django.contrib import admin
from . models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'reading_time')


admin.site.register(Blog, BlogAdmin)
