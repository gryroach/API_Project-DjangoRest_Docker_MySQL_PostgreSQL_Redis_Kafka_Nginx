import datetime

from rest_framework import serializers
from .models import JPHModel


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class JPHModelSerializer(serializers.ModelSerializer):
    update_date = serializers.ReadOnlyField()
    id = serializers.IntegerField(validators=[])

    class Meta:
        model = JPHModel
        fields = ['userId', 'id', 'title', 'body', 'update_date']

    def create(self, validated_data):
        update_date = datetime.datetime.now()
        return JPHModel.objects.create(update_date=update_date, **validated_data)

    def update(self, instance, validated_data):
        instance.update_date = datetime.datetime.now()
        instance.userId = validated_data.get('userId', instance.userId)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
