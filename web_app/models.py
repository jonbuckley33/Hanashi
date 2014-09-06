from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    discoverable = models.BooleanField(default=False)
    #location

class Conversation(models.Model):
    user_a = models.ForeignKey(User, related_name='conversation_a')
    user_b = models.ForeignKey(User, related_name='conversation_b')
    date_created = models.DateTimeField(auto_now=True)
    date_expired = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation)
    time_sent = models.DateTimeField(auto_now=True)
    text = models.TextField()
    sender = models.ForeignKey(User,related_name='+')
    recipient = models.ForeignKey('User',related_name='+')