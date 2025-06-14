from django.contrib import admin
from .models import Message, Notification, MessageHistory

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'parent_message', 'timestamp', 'edited')
    list_filter = ('edited',)
    search_fields = ('content', 'sender__username', 'receiver__username')

admin.site.register(Message, MessageAdmin)
admin.site.register(Notification)
admin.site.register(MessageHistory)