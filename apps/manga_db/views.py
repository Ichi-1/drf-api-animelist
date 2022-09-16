from apps.activity.serializers import CommentsListSerializer
from apps.anime_db.utils.paging import TotalCountHeaderPagination
from apps.activity.models import Comment
from core.serializers import EmptySerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Manga, MangaReview
from .serializers import (
    MangaDetailSerializer,
    MangaListSerializer,
    MangaReviewListSerializer
)


@extend_schema_view(
    list=extend_schema(summary='Get manga list'),
    retrieve=extend_schema(summary='Get manga details')
)
class MangaView(ModelViewSet):
    queryset = Manga.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = TotalCountHeaderPagination
    ordering = ["-average_rating"]  # default ordering
    lookup_field = "id"

    def get_serializer_class(self):
        if self.action == 'list':
            return MangaListSerializer
        if self.action == 'retrieve':
            return MangaDetailSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get manga comments list",
        description=(
            "If commentable resource has no comments, "
            "return empty list ```200 Ok```"
        )
    )
)
class MangaCommentsListView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = TotalCountHeaderPagination
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        manga_id = kwargs.get('id')
        commentable_manga = get_object_or_404(Manga, id=manga_id)
        comments = commentable_manga.comments.all().order_by('created_at')
        page = self.paginate_queryset(comments)
        serializer = self.get_serializer(page, many=True)
        # TODO Если комментариев к ресурсу нет - возвращается пустой массив
        return self.get_paginated_response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get manga reviews list",
        description=(
            "If reviewable resource has no review, "
            "return empty list ```200 Ok```"
        )
    )
)
class MangaReviewsListView(ModelViewSet):
    queryset = MangaReview.objects.all()
    serializer_class = MangaReviewListSerializer
    http_method_names = ["get"]


@extend_schema_view(
    put=extend_schema(
        summary="Update my favorites manga",
        description=(
            "Add specific manga to my favorites list. "
            "If manga alreadyt added to user favorites"
            "this endpoint does nothing and returns ```409 Conflict```"
        )
    ),
    delete=extend_schema(
        summary="Delete my favorites manga",
        description=(
            "If the specified anime does not exist in user's anime list"
            "this endpoint does nothing and returns ```404 Not Found```."
        ),
    ),

)
class MangaFavoritesView(GenericAPIView):
    http_method_names = ["put", "delete"]
    serializer_class = EmptySerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        manga_id = kwargs.get("id")
        manga = get_object_or_404(Manga, id=manga_id)
        user_favorites = manga.user_favorites.filter(id=request.user.id)

        if user_favorites.exists():
            return Response(
                {"detail": f"'{manga.title}' already added to favorites"},
                status=status.HTTP_409_CONFLICT
            )
        manga.user_favorites.add(request.user)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        manga_id = kwargs.get("id")
        manga = get_object_or_404(Manga, id=manga_id)
        user_favorites = manga.user_favorites.filter(id=request.user.id)

        if not user_favorites.exists():
            return Response(
                {"detail": f"'{manga.title}' not added to favorites"},
                status=status.HTTP_404_NOT_FOUND
            )
        manga.user_favorites.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
