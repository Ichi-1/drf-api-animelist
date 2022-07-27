from rest_framework.serializers import ModelSerializer
from apps.blog.models import Post


class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id', 
            'title',
            'category',
            'author', 
            'annotation', 
            'content', 
            'status',
        )