# Generated by Django 4.0.2 on 2022-02-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200, verbose_name='Street')),
                ('suite', models.CharField(max_length=200, verbose_name='Suite')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('zipcode', models.CharField(max_length=200, verbose_name='Zipcode')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('website', models.CharField(max_length=200, verbose_name='Website')),
                ('update_date', models.DateTimeField(null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drf_app.address', verbose_name='Address')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('catchPhrase', models.CharField(max_length=200, verbose_name='Catch phrase')),
                ('bs', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.IntegerField(verbose_name='Latitude')),
                ('lng', models.IntegerField(verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('body', models.TextField()),
                ('update_date', models.DateTimeField(null=True)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drf_app.author')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='JPHModel',
        ),
        migrations.AddField(
            model_name='author',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drf_app.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drf_app.geo', verbose_name='Geo'),
        ),
    ]
