# Generated by Django 5.0 on 2023-12-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndoorSensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=15)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=15)),
                ('co2', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
