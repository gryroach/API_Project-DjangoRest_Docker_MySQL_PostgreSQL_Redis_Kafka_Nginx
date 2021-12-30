import datetime

from rest_framework import serializers
from .models import JPHModel


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class JPHModelSerializer(serializers.ModelSerializer):
    update_date = serializers.ReadOnlyField(source='update_date.time')

    class Meta:
        model = JPHModel
        fields = ['userId', 'id', 'title', 'body', 'update_date']

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.update_date = datetime.datetime.now()
        instance.save()

    def is_valid(self, raise_exception=False, new=True):
        if new:
            return super(JPHModelSerializer, self).is_valid()
        else:
            return True
