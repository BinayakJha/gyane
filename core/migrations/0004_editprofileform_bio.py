# Generated by Django 3.2.8 on 2021-11-14 16:43

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_editprofileform_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='editprofileform',
            name='bio',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
