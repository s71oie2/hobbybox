from django.conf.urls import url
from .views import *

urlpatterns = [
    # Example: /
    url(r'^$', SearchFormView.as_view(), name='index'),

	# Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

	# Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]
