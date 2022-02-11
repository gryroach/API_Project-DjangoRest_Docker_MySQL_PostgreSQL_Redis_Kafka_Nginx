from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class Geo(models.Model):
    lat = models.IntegerField('Latitude')
    lng = models.IntegerField('Longitude')


class Address(models.Model):
    street = models.CharField('Street', max_length=200)
    suite = models.CharField('Suite', max_length=200)
    city = models.CharField('City', max_length=200)
    zipcode = models.CharField('Zipcode', max_length=200)
    geo = models.ForeignKey('Geo', on_delete=models.SET_NULL, verbose_name='Geo', null=True)


class Company(models.Model):
    name = models.CharField('Name', max_length=200)
    catchPhrase = models.CharField('Catch phrase', max_length=200)
    bs = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=255)
    username = models.CharField('Username', max_length=255)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=200)
    website = models.CharField('Website', max_length=200)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, verbose_name='Address')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name='Company')
    update_date = models.DateTimeField(null=True)

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    class Meta:
        ordering = ["id"]


class Post(models.Model):
    userId = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=240)
    body = models.TextField()
    update_date = models.DateTimeField(null=True)

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    class Meta:
        ordering = ["id"]
