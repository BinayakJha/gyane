# Generated by Django 3.2.8 on 2021-11-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211115_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
        migrations.AddField(
            model_name='note',
            name='note_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
