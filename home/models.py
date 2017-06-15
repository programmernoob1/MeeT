from django.db import models
from django.contrib.auth.models import User
from authentication.models import UserProfile
# Create your models here.
class Post(models.Model):
    userprofile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    body=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.pk