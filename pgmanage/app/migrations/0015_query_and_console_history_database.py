# Generated by Django 3.2.18 on 2024-02-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20231222_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='consolehistory',
            name='database',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='queryhistory',
            name='database',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
