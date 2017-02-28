
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import UserSerializer
from rest_framework import filters
class UserViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   filter_backends = (filters.SearchFilter,)
   search_fields = ('username',)