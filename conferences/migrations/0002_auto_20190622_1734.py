# Generated by Django 2.2.2 on 2019-06-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='registration_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conference',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
