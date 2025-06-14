from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from .models import Message

# Create your views here.
@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

# Recursive function to get nested replies
def get_replies_recursive(message):
    return [{
        'id': reply.id,
        'sender': reply.sender.username,
        'content': reply.content,
        'timestamp': reply.timestamp,
        'replies': get_replies_recursive(reply)
    } for reply in message.replies.all()]

@api_view(['GET'])
def get_threaded_conversation(request, user_id):
    current_user = request.user

    # Get top-level messages between users
    top_level_messages = (
        Message.objects
        .filter(
            sender__in=[current_user.id, user_id],
            receiver__in=[current_user.id, user_id],
            parent_message__isnull=True
        )
        .select_related('sender', 'receiver')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        )
        .order_by('timestamp')
    )

    # Format the data
    conversation = []
    for message in top_level_messages:
        conversation.append({
            'id': message.id,
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': message.timestamp,
            'replies': get_replies_recursive(message)
        })

    return Response(conversation)

@api_view(['GET'])
def unread_messages_view(request):
    user = request.user
    unread_messages = Message.unread.for_user(user)
    data = [
        {
            'id': msg.id,
            'sender': msg.sender.username,
            'content': msg.content,
            'timestamp': msg.timestamp
        }
        for msg in unread_messages
    ]
    return Response(data)