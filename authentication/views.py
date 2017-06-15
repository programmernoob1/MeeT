from django.shortcuts import render
from .forms import UserForm
from .nodes import UserNode
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
# Create your views here.
def index(request):
    context={}
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.session.get('login_failed')==True:
        context['login']=True
    user_form=UserForm()
    context['form']=user_form
    return render(request,'login.html',context)
def alogin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user:
        request.session['login_failed']=False
        login(request,user)
        return HttpResponseRedirect('/home/')
    else:
        request.session['login_failed']=True
        return HttpResponseRedirect('/auth/')
def register(request):
    user_form=UserForm(data=request.POST)
    if user_form.is_valid():
        username=request.POST['username']
        password=request.POST['password']
        user=user_form.save()
        user.set_password(request.POST['password'])
        user.save()
        userprofile=UserProfile.objects .create(user=user)
        newuser=UserNode(uid=userprofile.id)
        newuser.save()
        user = authenticate(username=username, password=password)
        request.session['login_failed'] = False
        login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        html='<h1>WRONG FORMAT</h1>'
        return HttpResponse(html)
def alogout(request):
    logout(request)
    return HttpResponseRedirect('/auth/')
