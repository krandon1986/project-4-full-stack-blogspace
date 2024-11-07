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

    # Posting comments
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create a comment object but not yet save to the database
            comment = comment_form.save(commit=False)
            # Display the commenters' name who is logged on
            comment.writer = request.user
            # Assign the current post written to the comment
            comment.post = post
            # Save the comment to the database
            comment.save()
            # Display a message to confirm the success of the posted comment
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment has been submitted and awaiting approval",
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

    # If form has been resubmitted after edited
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Comment can be updated if its comment form is valid
        # Writer's value is equal to the user's value
        if comment_form.is_valid() and comment.writer == request.user:
            comment.post = post
            comment.approved_comment = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        # Display the error message if the comment form is not valid
        # Writer's value isn't equal to the user's value
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Comment can be deleted if the writer's value is equal to the user's value
    # Display a success message for the comment deletion
    if comment.writer == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    # Display an error message if the values of both user and writer is not equal
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete you own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@login_required
def add_blog(request, slug=None):
    """
    Add a blog to the site
    """
    # If the user isn't a superuser, an error message will be displayed
    # Informing users that they don't have the authority to access the page
    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Sorry, only site owner can post blog on this site.",
        )
        return redirect(reverse("home"))

    # If the form has been submitted
    if request.method == "POST":
        # A form that is bounded to the POST data
        form = PostForm(request.POST, request.FILES)
        # All validation rules passes as the data is process in form.cleared data
        # Display a message to confirm the success of a new blog page
        if form.is_valid():
            post = form.save()
            messages.add_message(
                request, messages.SUCCESS, "Successfully added a new blog!"
            )
            return redirect(reverse("home"))
        # An error message will be displayed if validation rule isn't passed
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Failed to post a blog. Be sure the form is valid.",
            )
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
    # If the user isn't a superuser, an error message will be displayed
    # Informing users that they don't have the authority to access the page
    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Sorry, only site owner can post blog on this site.",
        )
        return redirect(reverse("home"))

    # If the form has been submitted
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        # A form that is bounded to the POST data
        form = PostForm(request.POST, request.FILES, instance=post)
        # All validation rules passes as the data is process in form.cleared data
        # Display a message to confirm the success of a updated blog page
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Successfully updated blog!"
            )
            return redirect(reverse("home"))
        # An error message will be displayed if validation rule isn't passed
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Failed to update the blog. Be sure the form is valid.",
            )
    else:
        form = PostForm(instance=post)
        messages.add_message(request, messages.INFO, f"You are editing {post.caption}")

    template = "blog/edit_blog.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """
    Edit a blog in the site
    """
    # If the user isn't a superuser, an error message will be displayed
    # Informing users that they don't have the authority to access the page
    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Sorry, only site owner can post blog on this site.",
        )
        return redirect(reverse("home"))

    # If the post on the form has been deleted
    # Display a message to confirm the successful deletion of a blog page
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.add_message(request, messages.SUCCESS, "Blog post deleted!")
    return redirect(reverse("home"))

