# Generated by Django 2.2.9 on 2020-02-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryday',
            name='training',
            field=models.BooleanField(),
        ),
    ]