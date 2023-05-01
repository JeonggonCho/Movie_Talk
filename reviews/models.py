from django.db import models
from django.conf import settings

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(null=False)
    movie = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='reviews/photos/')