from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview_image', 'created_at', 'is_published', 'views_counter')
    list_filter = ('created_at',)
    search_fields = ('title', 'content',)


