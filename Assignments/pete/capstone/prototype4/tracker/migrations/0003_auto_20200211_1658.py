# Generated by Django 2.2.9 on 2020-02-12 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200211_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryday',
            name='date',
            field=models.DateField(),
        ),
    ]
