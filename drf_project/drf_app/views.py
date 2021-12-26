import django.utils.datastructures
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

import io


from .models import JPHModel
from .serializers import MirrorSerializer, JPHModelSerializer
from .utils import download_json


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


@api_view(['GET'])
def sinch_post(request):
    posts = JPHModel.objects.all()
    list_of_id = []
    for post in posts:
        list_of_id.append(post.id)

    response = download_json()
    if isinstance(response, list):
        for post in response:
            content = JSONRenderer().render(post)
            stream = io.BytesIO(content)
            data = JSONParser().parse(stream)
            serializer = JPHModelSerializer(data=data)
            if post['id'] not in list_of_id:
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
    else:
        content = JSONRenderer().render(response)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = JPHModelSerializer(data=data)
        if response['id'] in list_of_id:
            return Response(data=f"Post with id {response['id']} is already exist", status=200)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(status=400)
    return Response(data=f"All posts downloaded", status=200)
