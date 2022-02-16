import django.utils.datastructures
import os

from django.http import Http404
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Author
from .serializers import MirrorSerializer, AuthorSerializer
from .src.utils import download_json
from .src.sync import sync_objects

posts_url = os.getenv('POSTS_API')
authors_url = os.getenv('AUTHORS_API')


@api_view(['GET'])
def mirror_text(request):
    if request.method == 'GET':
        try:
            text = {'text': request.GET['text']}
        except django.utils.datastructures.MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = MirrorSerializer(data=text)
        if serializer.is_valid():
            return Response(serializer.data)


class SyncPostView(APIView):

    def get(self, request):
        try:
            posts = download_json(posts_url)
        except Exception as er:
            return Response({'error': str(er)}, status=400)
        ex_posts = Post.objects.all()
        try:
            return sync_objects(posts, ex_posts, type_object='posts')
        except TypeError:
            return Response("Internal error. Unable to sync posts.", status=400)


class SyncAuthorView(APIView):

    def get(self, request):
        try:
            authors = download_json(authors_url)
        except Exception as er:
            return Response({'error': str(er)}, status=400)
        ex_authors = Author.objects.all()
        try:
            return sync_objects(authors, ex_authors, type_object='authors')
        except TypeError:
            return Response("Internal error. Unable to sync authors.", status=400)


class AuthorListView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        snippets = Author.objects.all()
        serializer = AuthorSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.create(serializer.validated_data)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            instance = serializer.create(serializer.validated_data)
            Author.objects.bulk_update([instance], ['name', 'username', 'email', 'phone', 'website', 'address',
                                                    'company', 'update_date'], batch_size=1)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
