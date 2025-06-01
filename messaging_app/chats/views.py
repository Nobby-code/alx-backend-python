from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import generics, viewsets, permissions




# from .models import Book
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework import status
# from .serializers import BookSerializer

# Create your views here.
# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list and create conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Add the authenticated user as a participant automatically
        conversation = serializer.save()
        conversation.participants.add(self.request.user)

    
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list and create messages for a conversation.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the sender of the message as the request user.
        """
        serializer.save(sender=self.request.user)

def home(request):
    return HttpResponse("Welcome to the API!")