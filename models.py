from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import  permalink
from django.contrib.auth.models import Permission, User
from time import timezone

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=128,)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    slug = models.SlugField(max_length=150,)
    postDetail = models.ForeignKey('blog.PostDetail',null=True,on_delete=models.CASCADE )


    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('blog:update', None, {'id':self.pk})


    @permalink
    def get_absolute_url(self):
        return ('blog:content', None, {'id':self.pk})



class PostDetail(models.Model):
    user = models.ForeignKey(User, default=1)
    category  = models.CharField(max_length=128)
    slug = models.SlugField(max_length=150, db_index=True,)

    def __str__(self):
        return self.category


    def get_product(self):
        return Post.objects.filter(category=self)


    @permalink
    def get_absolute_url(self):
        return ('blog:detail', None, { 'slug': self.slug })
    #
    # @permalink
    # def get_absolute_url(self):
    #     return ('blog:create', None, { 'slug': self.slug })


# class Comment(models.Model):
#     post = models

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    # email = models.EmailField(max_length=75, default=)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text