from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Tag(models.Model):
  value = models.TextField(max_length=100)

  def __str__(self):
    return self.value


class Comment(models.Model):
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id') # if above fields are named content_type and object_id than we could ommit the arguments on GenericForeignKey leaving it like - content_object = GenericForeignKey()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  published_at = models.DateTimeField(blank=True, null=True)
  title = models.TextField(max_length=100)
  slug = models.SlugField()
  summary = models.TextField(max_length=500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name='posts')
  comments = GenericRelation(Comment) # class model to be passed as GenericRelation argument must be defined above this class (on this case Comment class must be defined above Post class) or else it give an error

  def __str__(self):
    return self.title