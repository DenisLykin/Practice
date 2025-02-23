# Generated by Django 5.0.6 on 2024-07-06 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('house', models.IntegerField()),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.street')),
            ],
        ),
    ]
