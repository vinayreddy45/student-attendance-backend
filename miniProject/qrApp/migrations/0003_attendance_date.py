# Generated by Django 3.2.9 on 2021-11-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrApp', '0002_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
