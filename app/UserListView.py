from django.contrib.auth.models import User
from app.serializers import UserSerializer
from rest_framework import filters
from rest_framework import generics

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)