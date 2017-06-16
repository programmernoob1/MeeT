from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^sendreq$', views.sendreq),
    url(r'^friends$', views.friends),
    url(r'^accreq$', views.accreq),
    url(r'^canreq$', views.canreq),
]