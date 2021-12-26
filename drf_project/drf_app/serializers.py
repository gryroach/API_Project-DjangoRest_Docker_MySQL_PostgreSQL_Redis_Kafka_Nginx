from rest_framework import serializers
from .models import JPHModel


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class JPHModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JPHModel
        fields = ['userId', 'id', 'title', 'body']
