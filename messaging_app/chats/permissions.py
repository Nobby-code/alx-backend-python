from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission:
    - Only allow authenticated users who are part of the conversation.
    """

    def has_permission(self, request, view):
        '''Only allow authenticated users globally'''
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        '''For objects like Message or Conversation.
        Allow only if the user is one of the participants.'''
        # return obj.user == request.user or request.user in obj.participants.all()
        user_id = request.user.user_id
        # If obj is a Message, get its conversation
        if hasattr(obj, 'conversation'):
            # conversation = obj.conversation
            participants = obj.conversation.participants.all()
        else:
            # conversation = obj
            participants = obj.participants.all()
        return participants.filter(user_id=user_id).exists()
        # return user in conversation.participants.all()
        # return request.user in obj.participants.all()