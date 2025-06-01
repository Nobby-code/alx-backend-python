from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# Create your models here.
# class CustomUser(AbstractUser):
# User = get_user_model()
class User(AbstractUser):
    # Add custom fields here if needed, e.g. profile picture, phone, etc.
    # pass

    # bio = models.TextField(blank=True, null=True)
    # profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    def __str__(self):
        return self.username
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

# Conversation model
class Conversation(models.Model):
    participants = models.ManyToManyField('User', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"
    
# Messaging model
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender.username}"