from django import forms
from authentication.models import UserProfile
from django.contrib.auth.models import User
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('picture','nickname')
