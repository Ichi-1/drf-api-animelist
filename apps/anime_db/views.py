from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.contrib.contenttypes.models import ContentType

from apps.activity.models import Comment

from .models import Anime
from .utils.algolia import perform_serach
from .utils.filterset import AnimeListFilter
from .utils.paginator import TotalCountHeaderPagination
from .serializers import (
    AnimeDetailsSerializer,
    AnimeIndexSerializer,
    AnimeListSerializer,
    AnimeCommentsSerializer
)


class AnimeViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Anime.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_class = AnimeListFilter
    search_fields = ['title', '^title', 'year']
    ordering_fields = ['title', 'year', '?']
    pagination_class = TotalCountHeaderPagination
    ordering = ['-average_rating']  # default ordering

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimeListSerializer
        if self.action == 'retrieve':
            return AnimeDetailsSerializer



class AnimeCommentViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):  
    queryset = Comment
    serializer_class = AnimeCommentsSerializer
    pagination_class = TotalCountHeaderPagination
    lookup_field = 'commentable_id'
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve list of all comments belonging to anime which id is passed in query. 
        {commentable_id} - id of specific instance of Anime Model.
        Orber by: created_at
        """
        anime_id = kwargs.get('commentable_id')
        commentable = Anime.objects.get(id=anime_id)
        comments = commentable.comments.all().order_by('created_at')
        serializer = self.get_serializer(comments, many=True)

        if not serializer.data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)



class AlgoliaIndexAPIView(generics.GenericAPIView):
    serializer_class = AnimeIndexSerializer
    queryset = Anime.objects.all()

    def get(self, request):
        """
        Algolia index API for Anime Model
        """
        query = request.GET.get('search')
        tag = request.GET.get('tag')
        search_result = perform_serach(query=query, tags=tag)
        return Response(search_result)