# Generated by Django 5.0.1 on 2024-01-11 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Screenshots',
            fields=[
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, to='warcraftapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, to='warcraftapp.category')),
            ],
        ),
    ]