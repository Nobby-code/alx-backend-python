from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')

class Message(models.Model):
    '''Message model to define the message fields in a table
    '''
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # New field to check if a message has been edited
    edited = models.BooleanField(default=False)
    #New fiel to track if the message wa read
    read = models.BooleanField(default=False)

    #self-referential field to support replies
    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    objects = models.Manager()  # default manager
    unread = UnreadMessagesManager()  # custom manager
    def __str__(self):
        '''String readability for the message'''
        return f"New message from {self.sender} to {self.receiver}. Sent at: {self.timestamp} {self.content[:20]} !"


class Notification(models.Model):
    '''Notification model to notify the receiver of any new messages
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''String readability for notification'''
        return f"Notification for {self.user} - Message ID {self.message.id}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Message ID {self.message.id}"

