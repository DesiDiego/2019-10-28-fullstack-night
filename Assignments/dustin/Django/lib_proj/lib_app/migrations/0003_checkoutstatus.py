# Generated by Django 2.2.9 on 2020-02-18 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0002_auto_20200213_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=32)),
                ('time_out', models.TimeField(auto_now_add=True)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib_app.Book')),
            ],
        ),
    ]
