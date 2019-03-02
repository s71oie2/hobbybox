from django.conf.urls import url# 교과서 ch02 52쪽의 원래 코드를 아래와 같이 수정함
from . import views  # 이렇게 수정하면 아래 코드에서와 같이 views.~ 형식으로 변경해야 함
urlpatterns = [
    url(r'^$', views.NewsLV.as_view(), name='index'),
]