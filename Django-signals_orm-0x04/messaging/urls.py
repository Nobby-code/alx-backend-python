from django.urls import path
from .views import unread_messages_view, send_message

urlpatterns = [
    path('unread/', unread_messages_view, name='unread-messages'),
    path('send/', send_message, name='send-message'),
]