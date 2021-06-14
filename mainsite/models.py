from django.db import models
from django.contrib.auth.models import User

# Main blog site
class Blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pics")
    desc = models.TextField()


#Quotes on the banner of the Home Page
class Quote(models.Model):
    head = models.CharField(max_length = 100)
    one = models.TextField()
    two =models.TextField()
    three =models.TextField()

#Today's Special
class Header(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pics")
    before = models.TextField()
    after = models.TextField()

# About us in About Page
class About(models.Model):
    image= models.ImageField(upload_to="pics")
    desc = models.TextField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

# Our Team in About Page
class Team(models.Model):
    image= models.ImageField(upload_to="pics")   
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    name= models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    desc = models.TextField()

#Blog of Technology Page
class Tech(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pics")
    author = models.CharField(max_length=30)
    desc = models.TextField()

#Blog of Personality Page
class Person(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pics")
    author = models.CharField(max_length=30)
    desc = models.TextField()

#Blog of Random Page
class Random(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pics")
    author = models.CharField(max_length=30)
    desc = models.TextField()








