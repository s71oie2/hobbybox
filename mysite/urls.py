from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^review/', include('review.urls', namespace='review')),
    url(r'^hobby/', include('hobby.urls', namespace='hobby')),
    url(r'^dlivry/', include('dlivry.urls', namespace='dlivry')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^user/', include('user.urls', namespace='user')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

