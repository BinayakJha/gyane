# Generated by Django 3.2.10 on 2022-01-10 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20220102_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='note',
        ),
        migrations.RemoveField(
            model_name='question',
            name='note_editorjs_text',
        ),
    ]