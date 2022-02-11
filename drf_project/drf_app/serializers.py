from rest_framework import serializers
from .models import Author, Address, Company, Geo
from django.utils import timezone


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class GeoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Geo.objects.create(**validated_data)

    class Meta:
        model = Geo
        fields = ['lat', 'lng']


class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']


class CompanySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    class Meta:
        model = Company
        fields = ['name', 'catchPhrase', 'bs']


class AuthorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        geo_data = address_data.pop('geo', None)
        if geo_data:
            geo = Geo.objects.create(**geo_data)
            address_data['geo'] = geo
            print(geo)
        if address_data:
            address = Address.objects.create(**address_data)
            print(address)
            validated_data['address'] = address
        company_data = validated_data.pop('company', None)
        if company_data:
            company = Company.objects.create(**company_data)
            validated_data['company'] = company
        instance = Author(**validated_data)
        instance.update_date = timezone.now()
        instance.save()
        return instance

    class Meta:
        model = Author
        fields = ['id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date']
