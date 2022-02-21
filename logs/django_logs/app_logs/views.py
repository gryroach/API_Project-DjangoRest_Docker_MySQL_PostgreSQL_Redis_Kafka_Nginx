from rest_framework.decorators import api_view
from rest_framework.response import Response
from .src.kafka_consumer import consumer, consumer2, consumer3, consumer4


@api_view(['GET'])
def first(request):
    if request.method == 'GET':
        print(consumer)
        print(f'1 - {consumer.bootstrap_connected()}')
        print(f'1 - {consumer.bootstrap_connected()}')
        print(consumer.poll())
        return Response(str(consumer.bootstrap_connected()))


@api_view(['GET'])
def second(request):
    if request.method == 'GET':
        print(consumer2)
        print(f'2 - {consumer2.bootstrap_connected()}')
        print(f'2 - {consumer2.bootstrap_connected()}')
        print(consumer2.poll())
        return Response(str(consumer2.bootstrap_connected()))


@api_view(['GET'])
def third(request):
    if request.method == 'GET':
        print(consumer3)
        print(f'3 - {consumer3.bootstrap_connected()}')
        print(f'3 - {consumer3.bootstrap_connected()}')
        print(consumer3.poll())
        return Response(str(consumer3.bootstrap_connected()))


@api_view(['GET'])
def four(request):
    if request.method == 'GET':
        print(consumer4)
        print(f'4 - {consumer4.bootstrap_connected()}')
        print(f'4 - {consumer4.bootstrap_connected()}')
        print(consumer4.poll())
        return Response(str(consumer4.bootstrap_connected()))