import django_filters
from .models import Message
from django_filters.rest_framework import FilterSet

class MessageFilter(FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')
    sender = django_filters.NumberFilter(field_name="sender__id")
    conversation = django_filters.NumberFilter(field_name="conversation__id")

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'start_date', 'end_date']