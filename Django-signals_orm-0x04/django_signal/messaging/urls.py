from django.urls import path
from .views import unread_messages_view

urlpatterns = [
    path('unread/', unread_messages_view, name='unread-messages'),
]