# Generated by Django 2.2.9 on 2020-02-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_dos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateTimeField(null=True, verbose_name='date completed'),
        ),
    ]
