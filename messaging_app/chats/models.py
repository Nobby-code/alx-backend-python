from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# from django.contrib.auth import get_user_model

# Create your models here.
# class CustomUser(AbstractUser):
# User = get_user_model()
class User(AbstractUser):
    # Add custom fields here if needed, e.g. profile picture, phone, etc.
    # pass

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Conversation model
class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    participants = models.ManyToManyField('User', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"
    
# Messaging model
class Message(models.Model):
    # conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='messages')
    # content = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True)
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_body} from {self.sender.username}, Time:{self.sent_at}"