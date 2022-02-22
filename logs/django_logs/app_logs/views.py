from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .src.kafka_consumer import client, balanced_consumer
from .models import LogRecord


@api_view(['GET'])
def first(request):
    if request.method == 'GET':
        for message in balanced_consumer:
            if message is not None:
                print(message.offset, str(message.value))
                record = LogRecord(timestamp=timezone.now(), type_of_sync=message.value)
                record.save()

        return Response(str(client.topics))
