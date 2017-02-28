from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import  permalink

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128, unique=True )
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True,)
    postDetail = models.ForeignKey('blog.PostDetail',)


    def __str__(self):
        return self.title

    #@permalink
    # def get_absolute_url(self):
    #     return ('blog:detail', None, { 'slug': self.slug })




class PostDetail(models.Model):
    category  = models.CharField(max_length=128)
    slug = models.SlugField(max_length=150, db_index=True,)

    def __str__(self):
        return self.category




    def get_product(self):
        return Post.objects.filter(category=self)



    @permalink
    def get_absolute_url(self):
        return ('blog:detail', None, { 'slug': self.slug })





