from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    options = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blog_posts')
    annotation = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='./media/posts_images/%Y/%m/%d')
    slug = models.SlugField(max_length=255, unique_for_date='published')
    status = models.CharField(max_length=10, choices=options, default='published')
    published = models.DateTimeField(default=timezone.now)
    
    # default manager
    objects = models.Manager() 
    # custom manager 
    custom_objects = PostObjects() 
   
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
    