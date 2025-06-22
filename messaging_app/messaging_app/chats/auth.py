# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
        
#         # Use user_id instead of id
#         token['user_id'] = str(user.user_id)
#         return token
