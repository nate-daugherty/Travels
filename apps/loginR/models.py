# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors =[]

        if len(form_data["name"]) ==0:
            errors.append("Name is required.")

        if len(form_data["name"]) < 3:
            errors.append("Name must be atleast 3 characters..")

        
        if len(form_data["username"]) ==0:
            errors.append("Username is required.")

        
        if len(form_data["password"]) ==0:
            errors.append("Password is required.")

        if len(form_data["password"]) < 8:
            errors.append("Password must be atleast 8 characters.")

        if form_data["password"] != form_data["password_confirmation"]:
            errors.append("Password must match")

        return errors

    def create_user(self, form_data):
        hashedpw = bcrypt.hashpw(form_data["password"].encode(), bcrypt.gensalt())

        return User.objects.create(
            name= form_data["name"],
            username= form_data["username"],
            password = hashedpw,
        )

    def validate_login(self, form_data):
        errors = {}
        if len(form_data["username"]) ==0:
            errors.append("Username is required.")

        

        if len(form_data["password"]) < 8:
            errors.append("Password must be atleast 8 characters.")

        user = User.objects.filter(username = form_data["username"]).first()

        if user:

            if bcrypt.checkpw(form_data["password"].encode(), user.password.encode()):
                return {"user": user}
            
        return {"errors": errors}
    
class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)     
    password = models.CharField(max_length=45)     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    

class TravelManager(models.Manager):

    def validate_trip(self, form_data):
        errors = {}
        if len(form_data["destination"]) ==0:
            errors.append("Destination is required.")

        if len(form_data["description"]) ==0:
            errors.append("Description is required.")
        
        if len(form_data["departdate"]) ==0:
            errors.append("Date of departure is required.")

        if len(form_data["until"]) ==0:
            errors.append("When will you be returning?")

        return {"errors": errors}

    def create_trip(self, form_data):
        return Trip.objects.create(
            destination= form_data["name"],
            description= form_data["username"],
            departdate = form_data["departdate"],
            until = form_data["until"],
        )
     

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    departdate = models.DateField()
    until = models.DateField()
    user = models.ForeignKey(User, related_name="TRIP")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = TravelManager()


        
