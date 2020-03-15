# Generated by Django 3.0.3 on 2020-02-23 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('training', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diary_day', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('kcal', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carb', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('general', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(related_name='meal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diary_entry', to='tracker.DiaryDay')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diary_entry', to='tracker.Meal')),
            ],
        ),
    ]