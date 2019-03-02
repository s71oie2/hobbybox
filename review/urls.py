from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]