from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostByTagListView

# URL patterns for post function

urlpatterns = [
    path("", views.home, name="home"),

    # Authentication URLs
    
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Blog Post CRUD URLs

    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path("post/<int:pk>/comments/new/", views.CommentCreateView, name="add_comment"),
    path("comment/<int:pk>/update/", views.CommentUpdateView, name="update_comment"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView, name="delete_comment"),

    # Search URL
    path("search/", views.search_posts, name="search"),

    # By tag URL
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]