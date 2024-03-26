from django.contrib import admin
from .models import Post, Comment

# Registering Post Model
admin.site.register(Post)

# Registering Comment Model
admin.site.register(Comment)
