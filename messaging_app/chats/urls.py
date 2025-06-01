# chats/urls.py

from django.urls import path, include
# from rest_framework.routers import DefaultRouter
import rest_framework.routers as routers
from .views import ConversationViewSet, MessageViewSet

"""Automatically set routes for conversations.. post and get and messages
"""

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]
