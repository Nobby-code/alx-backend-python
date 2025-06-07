from rest_framework import serializers
# from .models import Book
from datetime import datetime, timezone
from .models import User, Conversation, Message
from django.contrib.auth import get_user_model

# class BookSerializer(serializers.ModelSerializer):
#     days_since_created = serializers.SerializerMethodField()

#     class Meta:
#         model = Book
#         # fields = '__all__'
#         fields = ['id', 'title', 'author', 'published_date', 'created_at', 'days_since_created']

#         def get_days_since_created(self, obj):
#             delta = datetime.now(timezone.utc) - obj.created_at
#             return delta.days

# User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email']


class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.StringRelatedField()  # Show username instead of ID
    message_body = serializers.CharField(max_length=1000)
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']
    
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email']


class ConversationSerializer(serializers.ModelSerializer):
    # participants = CustomUserSerializer(many=True, read_only=True)
    # messages = MessageSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)


    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']