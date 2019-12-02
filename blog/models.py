from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class FilePost(models.Model):
    title = models.CharField(max_length=20)
    file_data = models.FileField(null=False)

    def __str__(self):
        return self.title