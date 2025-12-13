from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    
        # Return notifications for the current user, ordered by newest first
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-timestamp")