from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.models import Album

from app.serializers import UserSerializer
from app.serializers import AlbumSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer


@api_view(['GET'])
def get_all_users(request):

    if request.method == 'GET':
       users = User.objects.all()
       serializer = UserSerializer(users, many=True)
       return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])    
def add_users(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully added', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])    
def search_users(request,username):
    # try:
    #     user = User.objects.get(username=username)
    # except user.DoesNotExist:
    #     return Response('Not found',status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = get_object_by_name(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

def get_object_by_name(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
            raise Http404

def get_object_by_id(id):
    try:
        return Album.objects.get(id=id)
    except User.DoesNotExist:
            raise Http404            
            
        
@api_view(['GET'])
def search(request,id):
    if request.method == 'GET':
       try:
           print("Parameter value=>"+request.data)
           album = get_object_by_id(id)
           serializer = AlbumSerializer(album)
       except Album.DoesNotExist:
           raise Http404 
       
       
       return Response(serializer.data)
    