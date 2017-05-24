from django.conf.urls import url, include
from django.contrib import admin
from .import views
app_name = 'users'



urlpatterns = [
             url(r'^$', views.UserFormView.as_view(),name='register'),
             url(r'^login_user/$', views.login_user,name='login'),
             url(r'^logout_user/$', views.logout_user,name='logout'),

]

