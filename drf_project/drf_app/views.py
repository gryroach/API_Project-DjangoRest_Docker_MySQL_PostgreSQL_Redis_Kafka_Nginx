from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MirrorSerializer


@api_view(['GET'])
def mirror_text(request):
    if request.method == 'GET':
        text = {'text': request.GET['text']}
        serializer = MirrorSerializer(data=text)
        if serializer.is_valid():
            return Response(serializer.data)
