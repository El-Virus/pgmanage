# Generated by Django 3.2.18 on 2023-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_connection_last_used_database'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='pigz_path',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
