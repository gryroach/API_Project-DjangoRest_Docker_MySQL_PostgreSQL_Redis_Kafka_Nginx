from rest_framework.decorators import api_view
from rest_framework.response import Response
from .src.kafka_consumer import client, balanced_consumer


@api_view(['GET'])
def first(request):
    if request.method == 'GET':
        for message in balanced_consumer:
            if message is not None:
                print(message.offset, str(message.value))

        return Response(str(client.topics))
