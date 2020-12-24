from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views


urlpatterns = [
    #登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    #注册页面
    url(r'^register/$', views.register, name='register'),

    #注销
    url(r'^login/$', views.logout_view, name='logout'),
]
