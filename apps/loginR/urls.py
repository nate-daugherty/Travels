from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^success$', views.success, name="dashboard"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^add$', views.add, name="add"),
]
