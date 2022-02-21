from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hello(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response('Hello')
