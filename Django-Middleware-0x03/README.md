Understanding Middlewares
Overview
Middleware is a powerful feature in application design that acts as a bridge between the request and response phases of the application cycle. In this project, learners will explore the concept of middleware, learn how to write custom middleware, and implement logic such as request interception, permission enforcement, request data filtering, logging, and more. Learners will also examine real-world use cases, such as authentication and rate-limiting, and understand the best practices when integrating middleware into a Django application.

This hands-on project will guide you in building a series of middleware components for an Airbnb Clone or similar web application, allowing them to understand middleware’s role in clean architecture and modular backend development.

Learning Objectives
By the end of this project, learners should be able to:

Understand the concept and lifecycle of middleware in Django.
Create custom middleware to intercept and process incoming requests and outgoing responses.
Filter and modify request/response data at the middleware level.
Implement access control mechanisms using middleware.
Use middleware to enforce API usage policies like rate limiting or request validation.
Integrate third-party middleware and understand Django’s default middleware stack.
Apply best practices for organizing middleware logic in a scalable project.
Learning Outcomes
Upon successful completion, learners will:

Define and explain how Django middleware works within the request/response cycle.
Write and integrate custom middleware in a Django project.
Use middleware to enforce permissions and restrict access based on roles, IP, or headers.
Filter and clean incoming request data before reaching the views.
Log request and response metadata for auditing or debugging purposes.
Separate concerns effectively using middleware rather than overloading views.
Evaluate the trade-offs and limitations of using middleware for certain functionalities.
Implementation Tasks
Learners will:

Scaffold a Django project with an apps/core structure for separation of concerns.
Build custom middleware to:
Log incoming requests and outgoing responses.
Restrict access to authenticated users or specific user roles.
Block requests from banned IPs or suspicious headers.
Modify or validate incoming JSON payloads.
Configure the MIDDLEWARE stack correctly in settings.py to include both built-in and custom middleware.
Test middleware behavior using Postman or Django’s test client to verify interception, modification, and rejection of requests.
Document middleware behavior using inline comments and Markdown files for clarity and maintainability.
Best Practices for Project Setup and Middleware Design
Here are some best practices to follow during implementation:

📁 Project Scaffolding Tips
Use a modular structure like:
  /project-root
    /apps
      /core
        /middleware
        /models
        /views
      /users
      /listings
    /config
    manage.py
Keep each custom middleware in a separate Python file under apps/core/middleware/ for clarity.
Use environment variables and Django settings to control behavior (e.g., toggle middleware for dev/production).
Middleware Best Practices
Keep middleware functions small and focused — avoid bloating a single middleware with multiple responsibilities.
Chain logic properly — always call get_response(request) unless rejecting the request early.
Use Django’s request.user, request.path, and request.method for clean conditional logic.
Avoid database-heavy logic in middleware to maintain performance.
Use logging middleware responsibly — log minimal and relevant data to avoid clutter.
Write unit tests for middleware behavior and edge cases.
Document each middleware clearly — what it does, why it exists, and where it sits in the stack.
Limitations and Considerations
While middleware can be powerful, it’s important to recognize its limitations:

Middleware shouldn’t replace views or serializers for business logic.
Middleware runs on every request, so poorly optimized code can degrade performance.
Order in MIDDLEWARE settings matters — incorrect ordering may break expected behavior.
Some functionalities are better suited for views, decorators, or DRF permissions.

Tasks
0. project set up
mandatory
Objective: Set up the django messaging app locally

Instructions:

Make a copy of the messaging_app directory done in the project Building Robust APIs,

Rename the copied directory to Django-Middleware-0x03

1. Logging User Requests(Basic Middleware)
mandatory
Objective: Create a middleware that logs each user’s requests to a file, including the timestamp, user and the request path.

Instructions: - create a file middleware.py and Create the middleware class RequestLoggingMiddleware with two methods, __init__and __call__.

In the __call__ implement a logger that log’s the following information f"{datetime.now()} - User: {user} - Path: {request.path}“

Configure the Middleware section in the settings.py with your newly created middleware

Run the server to test it out. python manage.py runserver

2. Restrict Chat Access by time
mandatory
Objective: implement a middleware that restricts access to the messaging up during certain hours of the day

Instructions:

Create a middleware class RestrictAccessByTimeMiddleware with two methods, __init__and__call__. that check the current server time and deny access by returning an error 403 Forbidden

if a user accesses the chat outside 9PM and 6PM.
Update the settings.py with the middleware.

3. Detect and Block offensive Language
mandatory
Objective: Implement middleware that limits the number of chat messages a user can send within a certain time window, based on their IP address.

Instructions:

Create the middleware class OffensiveLanguageMiddleware with two methods, __init__and__call__. that tracks number of chat messages sent by each ip address and implement a time based limit i.e 5 messages per minutes such that if a user exceeds the limit, it blocks further messaging and returns and error
use the __call__method to count the number of POST requests (messages) from each IP address.
Implement a time window (e.g., 1 minute) during which a user can only send a limited number of messages.
Ensure the middleware is added to theMIDDLEWARE setting in the settings.py

4. Enforce chat user Role Permissions
mandatory
Objective: define a middleware that checks the user’s role i.e admin, before allowing access to specific actions

Instructions:

Create the middleware class RolepermissionMiddleware with two methods, __init__ and __call__. that checks the user’s role from the request
If the user is not admin or moderator, it should return error 403
Ensure the middleware is added to the MIDDLEWARE setting in the settings.py