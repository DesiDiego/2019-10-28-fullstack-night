# Generated by Django 2.2.9 on 2020-02-06 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.DiaryDay')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.Meal')),
            ],
        ),
    ]