# Generated by Django 4.2.1 on 2023-06-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='year_of_creation',
            field=models.DateField(blank=True, null=True),
        ),
    ]
