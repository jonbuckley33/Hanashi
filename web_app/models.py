from django.db import models

class User(models.Model):
    username = models.CharField()
    password = models.CharField()
    date_created = models.DateTimeField(auto_now=True)
    discoverable = models.BooleanField(default=False)
    active_conversation = models.ForeignKey()
    #location

class Conversation(models.Model):
    user_a = models.ForeignKey()
    user_b = models.ForeignKey()
    date_created = models.DateTimeField(auto_now=True)
    date_expired = models.DateTimeField(auto_now=True)
    messageList = models.ForeignKey()