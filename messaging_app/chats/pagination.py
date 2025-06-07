from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20  # Number of messages per page
    page_size_query_param = 'page_size'  # Optional: client can set page size by this query param
    max_page_size = 100  # Optional: max page size allowed
