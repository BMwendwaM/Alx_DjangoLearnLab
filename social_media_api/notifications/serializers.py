from rest_framework import serializers
from .models import Notification

# Serializer for Notification model

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source="actor.username")
    
    class Meta:
        model = Notification
        fields = ["id", "actor", "verb", "timestamp"]