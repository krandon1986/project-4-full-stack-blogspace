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

    list_display = ('title', 'slug', 'status', 'created_on')
    search_field = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Registering Comment Model
admin.site.register(Comment)
