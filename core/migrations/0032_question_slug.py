# Generated by Django 3.2.10 on 2022-01-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20220111_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
