from django.conf.urls import url
from . import views  # 이렇게 수정하면 아래 코드에서와 같이 views.~ 형식으로 변경해야 함
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^create/$', views.UserRegistrationView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/verify/(?P<token>[0-9A-Za-z]{1,3}-[0-9A-Za-z]{1,20})/$', views.UserVerificationView.as_view()),
    url(r'^resend_verify_email/', views.ResendVerifyEmailView.as_view(), name='resend_verify_email'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^mail_cnf/$', views.UserEmailView.as_view(), name='mail_cnf'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]