# Generated by Django 2.2.9 on 2020-02-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200206_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('meas_sys', models.BooleanField()),
                ('weight', models.IntegerField()),
                ('bfp', models.IntegerField()),
                ('act_lvl', models.FloatField()),
                ('goal', models.BooleanField()),
                ('lbm', models.IntegerField()),
                ('bmr', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('train_kcal', models.IntegerField()),
                ('train_fat', models.IntegerField()),
                ('train_carb', models.IntegerField()),
                ('rest_kcal', models.IntegerField()),
                ('rest_fat', models.IntegerField()),
                ('rest_carb', models.IntegerField()),
            ],
        ),
    ]
