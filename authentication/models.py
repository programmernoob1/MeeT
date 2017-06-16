from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=50,blank=True)
    picture=models.ImageField(upload_to='profile_pics',default='facebook.jpg')
    def __str__(self):
        return self.user.username