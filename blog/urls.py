from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post_detail/<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('post_detail/<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('add/', views.add_blog, name='add_blog'),
    path('post_detail/edit/<slug:slug>/', views.edit_blog, 
        name='edit_blog'),
    path('post_detail/delete/<slug:slug>/', views.delete_blog, 
        name='delete_blog'),
]