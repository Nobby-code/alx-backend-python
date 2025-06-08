from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import generics, viewsets, permissions




# from .models import Book
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
from .pagination import MessagePagination
# from .serializers import BookSerializer

from .permissions import IsParticipantOfConversation

from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import IsParticipantOfConversation

from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.response import Response

# from .auth import CustomTokenObtainPairSerializer

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
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsParticipantOfConversation]
    
    def perform_create(self, serializer):
        # Add the authenticated user as a participant automatically
        conversation = serializer.save()
        conversation.participants.add(self.request.user)

    def get_queryset(self):
        '''Only return conversations the user is part of'''
        # return Conversation.objects.filter(participants=self.request.user.user_id)
        return Conversation.objects.filter(participants__user_id=self.request.user.user_id)

    
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list and create messages for a conversation.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [permissions.IsAuthenticated, IsParticipantOfConversation]
    permission_classes = [IsParticipantOfConversation]

    # Filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MessageFilter
    pagination_class = MessagePagination

    search_fields = ['content']
    ordering_fields = ['sent_at']
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['content']
    # ordering_fields = ['sent_at']

    #Filtering querysets
    def get_queryset(self):
        # return Message.objects.filter(sender=self.request.user) | Message.objects.filter(conversation__participants=self.request.user)
        # return Message.objects.filter(sender=self.request.user)
        '''Only return messages from conversations the user is part of'''
        # return Message.objects.filter(conversation__participants=self.request.user.user_id)
        return Message.objects.filter(conversation__participants__user_id=self.request.user.user_id)
        # '''Only return messages from conversations the user is part of'''
        # return Message.objects.filter(conversation__participants=self.request.user)
    
    def perform_create(self, serializer):
        """
        Save the sender as the current user after checking they belong to the conversation.
        """
        conversation_id = serializer.validated_data.get('conversation')

        # Ensure the user is a participant in the conversation
        if self.request.user not in conversation_id.participants.all():
            raise Response(
                {'detail': 'You are not allowed to send messages in this conversation!'},
                status=HTTP_403_FORBIDDEN
            )
        serializer.save(sender=self.request.user)


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

def home(request):
    return HttpResponse("Welcome to Middleware !")