# Generated by Django 3.1 on 2020-09-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
