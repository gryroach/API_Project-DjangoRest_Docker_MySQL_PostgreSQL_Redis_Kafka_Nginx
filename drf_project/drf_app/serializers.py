from rest_framework import serializers
from .models import Author, Address, Company, Geo


class MirrorSerializer(serializers.Serializer):
    text = serializers.CharField()


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ('lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):
    geo = serializers.RelatedField(source='Geo', read_only=True)

    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode', 'geo')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'catchPhrase', 'bs')


class AuthorSerializer(serializers.ModelSerializer):
    address = serializers.RelatedField(source='Address', read_only=True)
    company = serializers.RelatedField(source='Company', read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company')
