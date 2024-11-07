from django.shortcuts import ( 
    render, get_object_or_404, reverse, redirect
)
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
     Display an individual :model: `blog.Post`.

    **Context**

    ``post``
        An instance of :model: `blog.Post`.
    **Template:**

    :template: `blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved_comment=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.writer = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment.post = post
            comment.approved_comment = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.writer == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
        'You can only delete you own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def add_blog(request, slug=None):
    """
    Add a blog to the site
    """
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR,
            'Sorry, only site owner can post blog on this site.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.add_message(request, messages.SUCCESS,
                'Successfully added a new blog!')
            return redirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR,
             'Failed to post a blog. Be sure the form is valid.')
    else:
        form = PostForm()

    template = "blog/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)

@login_required
def edit_blog(request, slug):
    """
    Edit a blog in the site
    """
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR,
            'Sorry, only site owner can post blog on this site.')
        return redirect(reverse('home'))
    
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                'Successfully updated blog!')
            return redirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR,
             'Failed to update the blog. Be sure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.add_message(request, messages.INFO,
             f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)

@login_required
def delete_blog(request, slug):
    """
    Edit a blog in the site
    """
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR,
            'Sorry, only site owner can post blog on this site.')
        return redirect(reverse('home'))  

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.add_message(request, messages.SUCCESS,
        'Blog post deleted!')
    return redirect(reverse('home'))
