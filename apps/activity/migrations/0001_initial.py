# Generated by Django 4.0.6 on 2022-09-14 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commentable_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('santiment', models.CharField(choices=[('Positive', 'Positive'), ('Neutral', 'Neutral'), ('Negative', 'Negative')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='AnimeReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activity.review')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('activity.review',),
        ),
        migrations.CreateModel(
            name='MangaReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activity.review')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('activity.review',),
        ),
    ]
