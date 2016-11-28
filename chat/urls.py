from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.ChatUsersList.as_view()), name='chat_users_list'),
    url(r'^accounts/login/$', views.ChatLogin.as_view(), name='chat_login'),
    url(r'^users/(?P<to_user_id>\d+)$', login_required(views.ChatUsers.as_view()), name='chat_users'),
]