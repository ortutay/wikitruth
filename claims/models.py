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
    claim = models.ForeignKey(Claim)
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    body = models.TextField()
    citations = models.ManyToManyField(Claim, related_name='cited_by')
    # citations = models.ManyToManyField(
    #     Claim,
    #     through='Citation',
    #     through_fields=('response', 'claim'))
    timestamp = models.DateTimeField(auto_now_add=True)


# class Citation(models.Model):
#     response = models.ForeignKey(Response, on_delete=models.CASCADE)
#     claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
