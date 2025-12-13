from rest_framework import viewsets, filters
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# ViewSets for Post and Comment

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed View

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Get users that the current user is following
        following_users = user.following.all()

        # Filter posts
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
    

# Like/Unlike View

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Generate Notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )
            return Response({"message": "Post liked"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Check if like exists
        like = Like.objects.filter(user=request.user, post=post).first()
        
        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)