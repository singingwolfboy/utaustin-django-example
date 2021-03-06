from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()
    favorite_color = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "Profile for {user}".format(user=self.user)
