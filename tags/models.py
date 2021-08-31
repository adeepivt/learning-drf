from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.title
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


