from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .forms import PostForm
from authentication.nodes import UserNode,PostNode
from authentication.models import UserProfile
from django.http import HttpResponse,HttpResponseRedirect
from operator import attrgetter
from django.template.loader import render_to_string

from django.contrib.auth.models import User
# Create your views here.
# @login_required(login_url='/auth/')
def home(request):
    if request.method!='POST':
        post=PostForm()
        nodes = UserNode.nodes.all()
        profile=UserProfile.objects.get(user=request.user)
        user=UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
        friendnodes=user.friends.all()
        posts=[]
        for friend in friendnodes:
            for post in friend.posts.all():
                posts.append(Post(post.postedby.get().get_profile(),post))
        # friends=[]
        # for node in nodes:
        #     if not user.friends.is_connected(node) and node!=user:
        #         friends.append(UserProfile.objects.get(id=node.uid))
        post = PostForm()
        for i in user.posts.all():
            posts.append(Post(i.postedby.get().get_profile(), i))
        posts= sorted(posts, key=attrgetter('post.postdatetime'))
        posts=posts[::-1]
        html=render(request,'home.html',{'form':post,'user':user,'posts':posts})
        print(type(html))
        return html
    else:
        post=PostForm(request.POST)
        if post.is_valid():
            inst=PostNode(body=request.POST['body'])
            inst=inst.save()
            inst.postedby.connect(UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id))
            inst=inst.save()
            return HttpResponseRedirect('/home')
def sendreq(request):
    print("here at view")
    user = UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
    if request.method=='GET':
        id=request.GET['id']
    if id:
        enduser=UserNode.nodes.get(uid=id)
        if not user.requestsfrom.is_connected(enduser):
            user.requeststo.connect(enduser)
        else:
            user.friends.connect(enduser)
            user.requestsfrom.disconnect(enduser)
        user.save()
    return HttpResponse(reqrender(request))
def accreq(request):
    user = UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
    if request.method=='GET':
        id=request.GET['id']
    if id:
        enduser=UserNode.nodes.get(uid=id)
        if user.friends.is_connected(enduser):
            pass
        else:
            user.friends.connect(enduser)
            user.requestsfrom.disconnect(enduser)
            user.save()
    return HttpResponse(reqrender(request))
def canreq(request):
    user = UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
    if request.method=='GET':
        id=request.GET['id']
    if id:
        enduser=UserNode.nodes.get(uid=id)
        user.requeststo.disconnect(enduser)
        user.save()
    return HttpResponse(reqrender(request))

def friends(request):
    html=reqrender(request)
    return render(request, 'friends.html',{'html':html})
class Post(object):
    user=UserProfile()
    post=PostNode()
    def __init__(self,a,b):
        self.user=a
        self.post=b
def reqrender(request):
    user = UserNode.nodes.get(uid=UserProfile.objects.get(user=request.user).id)
    friendnodes = user.friends.all()
    friends = []
    for friend in friendnodes:
        friends.append(friend.get_profile())
    reqnodes = user.requestsfrom.all()
    requests = []
    for friend in reqnodes:
        requests.append(friend.get_profile())
    send = []
    nodes = UserNode.nodes.all()
    for friend in nodes:
        if friend not in reqnodes and friend not in friendnodes and friend != user:
            sent=0
            print(user.requeststo.is_connected(friend))
            if user.requeststo.is_connected(friend):
                sent=1
            else:
                sent=0
            print(sent)
            send.append(Send(friend.get_profile(),sent))
    rendered=render_to_string('friendstemplate.html',{'friends': user.friends.all(), 'requests': user.requestsfrom.all(), 'send':send})
    return rendered
class Send(object):
    user=UserProfile()
    def __init__(self,user,sent):
        self.user=user
        self.sent=sent