from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):

    POST_CATEGORIES = [
        ('TECH', 'Technology'),
        ('POLITICS', 'Politics'),
        ('TRAVEL', 'Travel'),
        ('SPORT', 'Sports')
    ]

    title = models.CharField(max_length=250, default='Example Title')
    publish_date = models.DateTimeField(auto_now_add=True)
    # description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20, choices=POST_CATEGORIES, default='TECH')
    image_url_1 = models.CharField(
        max_length=500, default='https://protkd.com/wp-content/uploads/2017/04/default-image.jpg')
    image_url_2 = models.CharField(
        max_length=500, default='https://protkd.com/wp-content/uploads/2017/04/default-image.jpg')

    def __str__(self):
        return self.title
