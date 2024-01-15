# Generated by Django 4.2.6 on 2024-01-12 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warcraftapp', '0002_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='warcraftapp.category'),
        ),
    ]
