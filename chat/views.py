from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Message

# Create your views here.


class ChatLogin(TemplateView):
    template_name = 'chat/login.html'


class ChatUsersList(TemplateView):
    template_name = 'chat/users_list.html'

    def get_context_data(self, **kwargs):
        return {'users': User.objects.exclude(pk=self.request.user.id)}


class ChatUsers(TemplateView):
    template_name = 'chat/users.html'

    def get_context_data(self, **kwargs):
        return {
            'messages': Message.get_conversation(self.request.user.id, kwargs['to_user_id']),
            'to_user_id': kwargs['to_user_id'],
        }

    def post(self, request, **kwargs):
        if Message.post(user_id=request.user.id, to_user_id=kwargs['to_user_id'], body=request.POST.get('body')):
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=500)

