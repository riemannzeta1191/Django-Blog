from django.conf.urls import url, include
from django.contrib import admin

from .import views
app_name = 'blog'

urlpatterns = [
    url(r'^$',"blog.views.post_list",name='index'),
    url(r'^(?P<id>\d+)/update/$', 'blog.views.post_update', name='update'),
    url(r'^create/$', 'blog.views.post_create', name='post_create'),
    url(r'^create/blog/posted/$', 'blog.views.form_redirect', name='form_redirect'),
    url(r'^post/(?P<id>\d+)/$', 'blog.views.view_post', name='content'),
    url(r'^search/', 'blog.views.searchResults', name='search'),
    url(r'^(?P<slug>[^\.]+)/$', views.post_detail.as_view(), name='detail'),


     # url(r'^search/', include('haystack.urls',)),
    # url(r'^create/$', "posts.views.post_create"),
    # url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
    # url(r'^(?P<id>\d+)/edit/$', "posts.views.post_update", name='update'),
    # url(r'^delete/$', "posts.views.post_delete"),
]