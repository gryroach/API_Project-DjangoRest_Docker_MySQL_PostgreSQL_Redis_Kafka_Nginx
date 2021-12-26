import datetime

import django.utils.datastructures
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import JPHModel
from .serializers import MirrorSerializer, JPHModelSerializer
from .utils import download_json, response_to_json


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
            data = response_to_json(post)
            serializer = JPHModelSerializer(data=data)
            if post['id'] not in list_of_id:
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
        return Response(data=f"All posts downloaded", status=200)
    elif isinstance(response, dict):
        data = response_to_json(response)
        serializer = JPHModelSerializer(data=data)
        if 'id' in response:
            if response['id'] in list_of_id:
                return Response(data=f"Post with id {response['id']} is already exist", status=200)
            else:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=200)
                else:
                    return Response(serializer.errors, status=400)
        else:
            return Response(data="API holder has no attribute 'id'", status=400)
    else:
        return Response(str(response.content).strip('\'b\''), status=400)


class SinchPostView(APIView):
    def get(self, request):
        posts = JPHModel.objects.all()
        list_of_id = []
        for post in posts:
            list_of_id.append(post.id)

        response = download_json()
        if isinstance(response, list):
            for post in response:
                data = response_to_json(post)
                serializer = JPHModelSerializer(data=data)
                if post['id'] not in list_of_id:
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)
            return Response(data=f"All posts downloaded", status=200)
        elif isinstance(response, dict):
            data = response_to_json(response)
            serializer = JPHModelSerializer(data=data)
            if 'id' in response:
                if response['id'] in list_of_id:
                    return Response(data=f"Post with id {response['id']} is already exist", status=200)
                else:
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=200)
                    else:
                        return Response(serializer.errors, status=400)
            else:
                return Response(data="API holder has no attribute 'id'", status=400)
        else:
            return Response(str(response.content).strip('\'b\''), status=400)

    def perform_create(self, serializer):
        serializer.save(update_date=datetime.datetime.now())
