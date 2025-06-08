from datetime import datetime
import logging
from django.http import HttpResponseForbidden
# from django.http import HttpResponseTooManyRequests
import time
from django.http import HttpResponse

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        '''Logger configuration'''
        self.logger = logging.getLogger("request_logger")
        handler = logging.FileHandler("requests.log")
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        print("Middleware is working...")

        self.logger.info(log_message)
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    '''Resrict chats access between 6pm and 9pm'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current server hour (0-23)
        current_hour = datetime.now().hour

        # Restrict access if current time is outside 18PM - 21PM
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Access to the chat is only allowed between 6PM and 9PM.")

        # Proceed with the request
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    ''''''
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store IP address as key, and a list of timestamps of their messages
        self.ip_message_log = {}

    def __call__(self, request):
        # Only restrict POST requests (usually sending messages)
        if request.method == "POST" and request.path.startswith("/api/messages/"):
            ip = self.get_client_ip(request)
            now = time.time()

            # Get the list of timestamps for this IP
            timestamps = self.ip_message_log.get(ip, [])

            # Filter timestamps to only keep those within the last 60 seconds
            timestamps = [t for t in timestamps if now - t < 60]

            # Check if the IP has sent 5 or more messages in the last minute
            if len(timestamps) >= 5:
                return HttpResponse("You have exceeded the message limit. Try again later.", status=429)

            # Add current timestamp to the list and update the log
            timestamps.append(now)
            self.ip_message_log[ip] = timestamps

        return self.get_response(request)

    def get_client_ip(self, request):
        # Get IP address from request headers (standard logic)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip


class RolePermissionMiddleware:
    '''middleware that checks the user’s role i.e admin, before allowing access to specific actions'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip permission check for unauthenticated users
        if request.user.is_authenticated:
            # Access the user's role
            user_role = getattr(request.user, 'role', None)

            # Example: Only allow "admin" or "moderator" for sensitive paths
            protected_paths = ['/api/conversations/', '/api/messages/']

            if any(request.path.startswith(path) for path in protected_paths):
                if user_role not in ['admin', 'moderator']:
                    return HttpResponseForbidden("Access denied: insufficient permissions.")

        # Proceed to the next middleware or view
        return self.get_response(request)