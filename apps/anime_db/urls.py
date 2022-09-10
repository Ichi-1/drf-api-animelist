from django.urls import path
from .views import AlgoliaIndexAPIView
from .router import (
    anime_list,
    anime_detail,
    anime_comments_list,
)

app_name = 'anime_db'

#   TODO роутинг ModelViewSet выносится в отдельный router.py

urlpatterns = [
    path('anime/', anime_list),
    path('anime/<int:id>/', anime_detail),
    path('anime/index/', AlgoliaIndexAPIView.as_view()),
    path('anime/<int:id>/comments/', anime_comments_list),
    # path('anime/<int:id>/reviews', reviews_list_or_create),
]
