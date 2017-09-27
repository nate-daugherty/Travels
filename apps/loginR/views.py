# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import *

# Create your views here.
def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def index(request):
    return render(request, "loginR/index.html")

def register(request):
    if request.method == "POST":
            #validate form data
        errors= User.objects.validate_registration(request.POST)
            #check if errors dont exist
    if not errors:
        user = User.objects.create_user(request.POST)
                #create the user
                #log in the user
        request.session["user_id"]= user.id
                #redirect to success page
        return redirect(reverse("landing"))

            #flash errors
    flash_errors(errors, request)
            #redirect main page

    return redirect(reverse("dashboard"))

def success(request):
    if "user_id" in request.session:
        context ={
            "user": current_user(request),
        }
        
        return render(request, "loginR/success.html", context)
    return redirect(reverse("landing"))
def current_user(request):
    return User.objects.get(id= request.session["user_id"])

def login(request):
    if request.method =="POST":
        check = User.objects.validate_login(request.POST)

        if "user" in check:

            request.session["user_id"] = check["user"].id

            return redirect(reverse("dashboard"))

        flash_errors(check["errors"], request)

    return redirect(reverse("landing"))

def logout(request):
    request.session.flush()

    return redirect(reverse("landing"))

def add(request):
    return render(request, "loginR/add.html")


def createTrip(request):
    if request.method =="POST":
        check= Trip.objects.validate_trip(request.POST)

        if "trip" in check:

            request.session["trip_id"] = check["trip"].id

            return redirect(reverse("dashboard"))

        flash_errors(check["errors"], request)

    return redirect(reverse("landing"))

