import django.utils.datastructures
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Author
from .serializers import MirrorSerializer
from .src.utils import download_json
from .src.sync import sync_posts, sync_authors

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
        posts = download_json(posts_url)
        ex_posts = Post.objects.all()
        try:
            return sync_posts(posts, ex_posts)
        except TypeError:
            return Response(str(posts.content).strip('\'b\''), status=400)


class SyncAuthorView(APIView):

    def get(self, request):
        authors = download_json(authors_url)
        ex_authors = Author.objects.all()
        try:
            return sync_authors(authors, ex_authors)
        except TypeError:
            return Response(str(authors.content).strip('\'b\''), status=400)


