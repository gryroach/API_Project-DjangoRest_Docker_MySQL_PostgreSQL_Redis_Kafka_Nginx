from rest_framework import serializers
from .models import JPHModel


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class JPHModelSerializer(serializers.ModelSerializer):
    update_date = serializers.ReadOnlyField(source='update_date.time')

    class Meta:
        model = JPHModel
        fields = ['userId', 'id', 'title', 'body', 'update_date']
