# Generated by Django 3.0.3 on 2020-03-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200310_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/{user.username}'),
        ),
    ]
