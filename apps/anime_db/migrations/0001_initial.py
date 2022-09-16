# Generated by Django 4.0.6 on 2022-09-16 13:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age_rating', models.CharField(max_length=5, verbose_name='Age Rating')),
                ('age_rating_guide', models.CharField(max_length=50, verbose_name='Age Rating Guidence')),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Average Rating')),
                ('description', models.TextField(verbose_name='Description')),
                ('episode_count', models.IntegerField(verbose_name='Episodes count')),
                ('episode_length', models.IntegerField(verbose_name='Episode length')),
                ('kind', models.CharField(max_length=10, verbose_name='Show Type')),
                ('poster_image', models.URLField(max_length=255, verbose_name='Poster URL')),
                ('season', models.CharField(max_length=20, null=True, verbose_name='Realese season')),
                ('staff', models.TextField(null=True, verbose_name='Staff Team')),
                ('studio', models.CharField(max_length=50, null=True, verbose_name='Studio')),
                ('tags', models.TextField(null=True, verbose_name='Genres Tags')),
                ('title', models.CharField(max_length=255, verbose_name='English title')),
                ('title_jp', models.CharField(max_length=255, verbose_name='Japan title')),
                ('total_length', models.IntegerField(verbose_name='Total length')),
                ('voice_actors', models.TextField(null=True, verbose_name='Voice Actors')),
                ('year', models.PositiveIntegerField(null=True, verbose_name='Release year')),
                ('year_end', models.PositiveIntegerField(null=True, verbose_name='Airing end year')),
                ('user_favorites', models.ManyToManyField(blank=True, related_name='favorites_anime', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Anime',
            },
        ),
        migrations.CreateModel(
            name='MyAnimeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(choices=[(0, 'Not Rated'), (1, 'Awful'), (2, 'Pretty Bad'), (3, 'So So'), (4, 'Good'), (5, 'Masterpiece')], default=0, verbose_name='Item score in list')),
                ('note', models.TextField(max_length=300, verbose_name='My note about item')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Watching', 'Watching'), ('Plan to watch', 'Plan To Watch'), ('Completed', 'Completed'), ('Dropped', 'Dropped')], max_length=15)),
                ('num_episodes_watched', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Number of watched episodes')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_db.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimeReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activity.review')),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anime_review', to='anime_db.anime')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('activity.review',),
        ),
    ]
