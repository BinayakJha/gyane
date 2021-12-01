# Generated by Django 3.2.8 on 2021-11-16 04:31

from django.db import migrations, models
import django_quill.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_note_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuillPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
            ],
        ),
        migrations.AlterField(
            model_name='editprofileform',
            name='bio',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]