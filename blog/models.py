from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    POST_CATEGORIES = [
        ('TECH', 'Technology'),
        ('POLITICS', 'Politics'),
        ('TRAVEL', 'Travel'),
        ('SPORT', 'Sports')
    ]

    title = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20, choices=POST_CATEGORIES, default='TECH')

    def __str__(self):
        return self.title
