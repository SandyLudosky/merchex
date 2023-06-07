# Generated by Django 4.2.1 on 2023-06-02 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_year_of_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='year_of_creation',
        ),
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(blank=True, choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]