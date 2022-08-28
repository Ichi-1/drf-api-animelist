from apps.anime_db.models import Anime
from django_filters import rest_framework as filters


class AnimeFilter(filters.FilterSet):
    year = filters.RangeFilter()
    tags = filters.CharFilter(lookup_expr='in')

    class Meta:
        model = Anime
        fields = ['year', 'tags', 'kind']