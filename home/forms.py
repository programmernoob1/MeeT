from django import forms
from . import models
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=('body',)
