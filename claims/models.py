from django.db import models
from django.contrib.auth.models import User

DIRECTION_CHOICES = ((
    ('agree', 'Agree'),
    ('disagree', 'Disagree'),
))


class Claim(models.Model):
    thesis = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thesis


class Response(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    claim = models.ForeignKey(Claim)
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    body = models.TextField()
    citations = models.ManyToManyField(Claim, related_name='cited_by')


class Comment(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.ForeignKey(Response)
    parent = models.ForeignKey('Comment', null=True)
    body = models.TextField()
