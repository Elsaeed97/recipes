"""
    Contains Views for users API
"""
from rest_framework import generics
from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create User API view. """
    serializer_class = UserSerializer
