# Generated by Django 3.2.10 on 2022-01-14 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_alter_profile_small_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]