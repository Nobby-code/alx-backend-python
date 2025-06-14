from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    '''Listens to the new message being saved and sends notification to the receivers
    '''
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    '''Log the previous message before edit'''
    if instance.pk:
        try:
            old_instance = Message.objects.get(pk=instance.pk)
            if old_instance.content != instance.content:
                instance.edited = True
                MessageHistory.objects.create(
                    message=old_instance,
                    old_content=old_instance.content
                )
        except Message.DoesNotExist:
            pass  # It’s a new message, nothing to log

@receiver(post_delete, sender=User)
def delete_related_data(sender, instance, **kwargs):
    # Delete messages where the user was sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications belonging to the user
    Notification.objects.filter(user=instance).delete()

    # Delete message histories for messages sent or received by this user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()