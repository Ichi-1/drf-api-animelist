# Generated by Django 4.0.6 on 2022-09-16 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymangalist',
            name='num_chapters_read',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(7774)], verbose_name='Number of readed chapters'),
        ),
    ]