from django import forms
from django.db.models import fields
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "desc", "image"]
        labels = {
            "title": "Title",
            "desc": "Description",
            "image": "Image",
        }

class HeadForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['title', 'image', 'before', 'after']
        labels = {'title': 'Title', 'image':"Image", "before": "Before", "after":"After"}

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image', 'desc', 'facebook', 'twitter', 'linkedin']
        labels = {'image': 'Image', 'facebook':'Facebook', 'twitter':'Twitter', 'linkedin':'Linkedin'}

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['image', 'name', 'position', 'desc', 'facebook', 'twitter', 'linkedin']
        labels = {'image':"Image", 'name': 'Name', 'position': 'Position', 'desc': 'Description', 'facebook':'Facebook', 'twitter':'Twitter', 'linkedin':'Linkedin'}

class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = ['title', 'image','desc', 'author']
        labels = {'title': 'Title', 'image':"Image", 'desc': 'Description', 'author':'Author'}

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'image','desc', 'author']
        labels = {'title': 'Title', 'image':"Image", 'desc': 'Description', 'author':'Author'}

class RandomForm(forms.ModelForm):
    class Meta:
        model = Random
        fields = ['title', 'image','desc', 'author']
        labels = {'title': 'Title', 'image':"Image", 'desc': 'Description', 'author':'Author'}

