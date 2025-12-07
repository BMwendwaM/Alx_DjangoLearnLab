from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag




# View for Post Model - home page

def home(request):
    return render(request, 'blog/base.html')



# Register and Profile Views


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created!")
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "blog/profile.html", context)



# Views for CRUD operations on Blog Posts.


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    

# CRUD Views for Comments on Posts
# ADD YOUR COMMENT VIEW

@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Don't save yet
            comment.author = request.user      # Set logged-in user
            comment.post = post                # Link to post
            comment.save()                     # Save to database
            messages.success(request, "Comment added successfully!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comment_form.html", {"form": form})


# EDIT YOUR COMMENT VIEW

@login_required
def CommentUpdateView(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    # Only allow the author to edit

    if comment.author != request.user:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect("post_detail", pk=comment.post.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/comment_form.html", {"form": form})

# DELETE YOUR COMMENT VIEW

@login_required
def CommentDeleteView(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.author != request.user:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect("post_detail", pk=comment.post.pk)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect("post_detail", pk=comment.post.pk)

    return render(request, "blog/comment_delete.html", {"comment": comment})


# Search View - by multiple parameters

def search_posts(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, "blog/search_results.html", {"query": query, "results": results})

# View to filter posts by tag


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})
