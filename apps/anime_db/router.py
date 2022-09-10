from .views import AnimeViewSet, AnimeCommentsViewSet


anime_list = AnimeViewSet.as_view(
    {
        "get": "list"
    }
)

anime_detail = AnimeViewSet.as_view(
    {
        "get": "retrieve"
    }
)

anime_comments_list = AnimeCommentsViewSet.as_view(
    {
        "get": "list"
    }
)
