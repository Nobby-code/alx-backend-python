from django.contrib import admin
from .models import User, Conversation, Message

# Register your models here.
# admin.site.register(User)
# admin.site.register(Conversation)
# admin.site.register(Message)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name')
    ordering = ('user_id',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'conversation', 'sender', 'sent_at')