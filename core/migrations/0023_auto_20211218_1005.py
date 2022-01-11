# Generated by Django 3.2.10 on 2021-12-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='note_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
