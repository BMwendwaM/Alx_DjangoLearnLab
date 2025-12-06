from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

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
    path("posts/<int:post_id>/comments/new/", views.CommentCreateView, name="add_comment"),
    path("comment/<int:pk>/edit/", views.CommentUpdateView, name="edit_comment"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView, name="delete_comment"),
]