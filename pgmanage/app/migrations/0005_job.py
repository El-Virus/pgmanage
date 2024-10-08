# Generated by Django 2.2.28 on 2023-02-15 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_confighistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('command', models.TextField()),
                ('description', models.TextField()),
                ('arguments', models.TextField(blank=True)),
                ('logdir', models.TextField()),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('exit_code', models.IntegerField(null=True)),
                ('utility_pid', models.IntegerField(null=True)),
                ('process_state', models.IntegerField(null=True)),
                ('connection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Connection')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
