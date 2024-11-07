from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Creating a Post model
class Post(models.Model):
    """
    Store a single blog post entry related to :model: `auth.User`.
    """
    caption = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    chosen_image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.caption} | posted by {self.writer}"

# Creating a Comment Model
class Comment(models.Model):
    """
    Store a single comment entry related to :model: `auth.User`
    and :model: `blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    body = models.TextField()
    approved_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.body} by {self.writer}"
