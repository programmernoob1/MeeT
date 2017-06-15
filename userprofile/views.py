from authentication.nodes import UserNode
from django.shortcuts import render
from authentication.models import UserProfile
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserProfileForm
# Create your views here.
def home(request):
    user = UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
    form=UserProfileForm()
    return render(request,'profile.html',{'form':form,'profile':user.get_profile()})
def edit(request):
    profiles = UserProfile.objects.filter(user=request.user)
    form=UserProfileForm(request.POST,request.FILES,instance=profiles[0])
    form.save()
    return HttpResponseRedirect('/profile/')