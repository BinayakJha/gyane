# Generated by Django 3.2.8 on 2021-11-16 04:25

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_editprofileform_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
