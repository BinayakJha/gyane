# Generated by Django 3.2.10 on 2022-01-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='note_editorjs',
            new_name='question',
        ),
    ]
