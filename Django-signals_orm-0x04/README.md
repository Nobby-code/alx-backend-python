Tasks
0. Implement Signals for User Notifications
mandatory
Objective: Automatically notify users when they receive a new message.

Instructions:

Create a Message model with fields like sender, receiver, content, and timestamp.

Use Django signals (e.g., post_save) to trigger a notification when a new Message instance is created.

Create a Notification model to store notifications, linking it to the User and Message models.

Write a signal that listens for new messages and automatically creates a notification for the receiving user.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: messaging/models.py, messaging/signals.py, messaging/apps.py, messaging/admin.py, messaging/tests.py

1. Create a Signal for Logging Message Edits
mandatory
Objective: Log when a user edits a message and save the old content before the edit.

Instructions:

Add an edited field to the Message model to track if a message has been edited.

Use the pre_save signal to log the old content of a message into a separate MessageHistory model before it’s updated.

Display the message edit history in the user interface, allowing users to view previous versions of their messages.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: Django-Chat/Models

2. Use Signals for Deleting User-Related Data
mandatory
Objective: Automatically clean up related data when a user deletes their account.

Instructions:

Create a delete_user view that allows a user to delete their account.

Implement a post_delete signal on the User model to delete all messages, notifications, and message histories associated with the user.

Ensure that foreign key constraints are respected during the deletion process by using CASCADE or custom signal logic.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: Django-Chat/Views

3. Leverage Advanced ORM Techniques for Threaded Conversations
mandatory
Objective: Implement threaded conversations where users can reply to specific messages, and retrieve conversations efficiently.

Instructions:

Modify the Message model to include a parent_message field (self-referential foreign key) to represent replies.

Use prefetchrelated and selectrelated to optimize querying of messages and their replies, reducing the number of database queries.

Implement a recursive query using Django’s ORM to fetch all replies to a message and display them in a threaded format in the user interface.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: Django-Chat/Models

4. Custom ORM Manager for Unread Messages
mandatory
Objective: Create a custom manager to filter unread messages for a user.

Instructions:

Add a read boolean field to the Message model to indicate whether a message has been read.

Implement a custom manager (e.g., UnreadMessagesManager) that filters unread messages for a specific user.

Use this manager in your views to display only unread messages in a user’s inbox.

Optimize this query with .only() to retrieve only necessary fields.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: Django-Chat/Models

5. implement basic view cache
mandatory
Objective: Set up basic caching for a view that retrieves messages in the messaging app.

Instructions:

Update your settings.py in your messagingapp/messagingapp/settings.py with the default cache i.e django.core.cache.backends.locmem.LocMemCache as follows:
CACHES = { 'default': { 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache', 'LOCATION': 'unique-snowflake', } }

Use cache-page in your views to cache the view that displays a list of messages in a conversation. Learn more about cache-page here

Set a 60 seconds cache timeout on the view.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: messaging_app/messaging_app/settings.py, chats/views.py

