from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, null=False, related_name='sender')
    to_user = models.ForeignKey(User, null=False, related_name='receiver')
    body = models.TextField(null=False, blank= False)

    created_at = models.DateTimeField(auto_now_add=True, null=False)

    @classmethod
    def get_conversation(cls, user_id, to_user_id):
        return cls.objects.filter(user_id__in= [user_id, to_user_id], to_user_id__in=[user_id, to_user_id]).\
            order_by('created_at')

    @classmethod
    def post(cls, user_id, to_user_id, body):
        message = cls(user_id=user_id, to_user_id=to_user_id, body=body)
        message.save()
        if message.pk:
            return True
        else:
            return False
