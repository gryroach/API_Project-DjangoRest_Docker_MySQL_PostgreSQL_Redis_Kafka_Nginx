from rest_framework import serializers


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()
