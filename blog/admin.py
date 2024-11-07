from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Updating the admin page's layout and format
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filter, fields to prepopulate and rich-text editor.
    """

    list_display = ('caption', 'slug', 'status', 'created_at')
    search_field = ['caption', 'body']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {'slug': ('caption',)}
    summernote_fields = ('body',)

# Registering Comment Model
admin.site.register(Comment)
