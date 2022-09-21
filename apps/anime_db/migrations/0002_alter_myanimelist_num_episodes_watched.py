# Generated by Django 4.0.6 on 2022-09-16 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myanimelist',
            name='num_episodes_watched',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Number of watched episodes'),
        ),
    ]