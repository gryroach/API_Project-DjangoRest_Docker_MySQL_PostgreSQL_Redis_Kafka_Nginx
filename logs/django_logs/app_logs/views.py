from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .src.kafka_consumer import client, balanced_consumer
from .models import LogRecord
# from .src.threads import thread_log
from .src.threads import CreateLogsThread


@api_view(['GET'])
def first(request):
    if request.method == 'GET':
        CreateLogsThread().start()

        return Response(str('ok'))

