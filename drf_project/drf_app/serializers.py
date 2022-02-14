from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Author, Address, Company, Geo, Post
from django.utils import timezone


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = ['lat', 'lng']

    def create(self, validated_data):
        return Geo.objects.create(**validated_data)


class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['name', 'catchPhrase', 'bs']

        extra_kwargs = {
            'name': {'validators': [ValidationError]},
        }

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['userId', 'id', 'title', 'body', 'update_date']

        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        instance = Post(**validated_data)
        instance.update_date = timezone.now()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()
    userId = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date', 'userId']

        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        geo_data = address_data.pop('geo', None)
        if geo_data:
            try:
                geo = Geo.objects.get(lat=geo_data['lat'], lng=geo_data['lng'])
            except Geo.DoesNotExist:
                geo = Geo.objects.create(**geo_data)
            address_data['geo'] = geo
        if address_data:
            try:
                address = Address.objects.get(street=address_data['street'], suite=address_data['suite'],
                                              city=address_data['city'], zipcode=address_data['zipcode'])
            except Address.DoesNotExist:
                address = Address.objects.create(**address_data)
            validated_data['address'] = address
        company_data = validated_data.pop('company', None)
        if company_data:
            try:
                company = Company.objects.get(name=company_data['name'])
            except Company.DoesNotExist:
                company = Company.objects.create(**company_data)
            validated_data['company'] = company
        instance = Author(**validated_data)
        instance.update_date = timezone.now()
        return instance
