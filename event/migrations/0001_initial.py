# Generated by Django 5.0.1 on 2024-02-04 16:38

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Event Posters')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('starting_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('published', models.BooleanField(blank=True, default=False, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('event_poster', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Event Posters')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='event_details', to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_pictures', to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventSNS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.TextField(blank=True, null=True)),
                ('facebook', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('youtube', models.TextField(blank=True, null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='event_social_media', to='event.event')),
            ],
        ),
    ]
