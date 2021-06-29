from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *

def index(request):
    header =  Header.objects.all()
    blog = Blog.objects.all()
    quote = Quote.objects.all()
    return render(request, 'index.html', {'blogs': blog, 'quote': quote, 'headers': header})

def contact(request):
    about = About.objects.all()
    return render(request, 'contact.html',{"about": about})

def about(request):
    team = Team.objects.all()
    about = About.objects.all()
    return render(request, 'about.html',{'about': about,'team': team})   


def dashboard(request):
    if request.user.is_superuser:
        header =  Header.objects.all()
        blog = Blog.objects.all()
        tech = Tech.objects.all()
        person = Person.objects.all()
        random = Random.objects.all()
        team = Team.objects.all()
        about = About.objects.all()
        context = {'header': header, 'blog': blog, 'tech': tech, 'person': person, 'random': random, 'team': team, 'about': about}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponse("You don't have access for this site..")


def technology(request):
    techs = Tech.objects.all()
    return render(request, 'technology.html', {'techs': techs})

def personality(request):
    persons = Person.objects.all()
    return render(request, 'personality.html', {'persons': persons})

def random(request):
    randoms = Random.objects.all()
    return render(request, 'random.html',{'randoms': randoms})

def about(request):
    team = Team.objects.all()
    about = About.objects.all()
    context = {'team': team, 'about': about}
    return render(request, 'about.html', context)


def contact_us(request):
    if request.method=="POST":
        username =request.POST['username']
        email =request.POST['username']
        subject = request.POST['subject']
        message = request.POST['message']
    # Send email
        send_mail(
            subject,
            message,
            email,
            ['nepalprabhu123@gmail.com'],
        )
        return render(request, 'contact.html', {'username': username})    
    else:
        return render(request,'contact.html')



def edit_blog(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Blog.objects.get(pk=id)
            form = PostForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        else:
            id = Blog.objects.get(pk=id)
            form = PostForm(instance=id)
            return render(request, 'edit_blog.html', {'form':form, 'blog': id})
            
    else:
        return HttpResponse("You don't have access for this site....")


def delete_blog(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            # pi =Blog.objects.get(pk=id)
            # pi.delete()
            Blog.objects.filter(id=id).delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_blog(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = PostForm()
        return render(request, 'add_blog.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_header(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Header.objects.get(pk=id)
            form = HeadForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = Header.objects.get(pk=id)
            form = HeadForm(instance=id)
            return render(request, 'edit_header.html', {'form':form, 'header': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_header(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =Header.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_header(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = HeadForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = HeadForm()
        return render(request, 'add_header.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_team(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Team.objects.get(pk=id)
            form = TeamForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = Team.objects.get(pk=id)
            form = TeamForm(instance=id)
            return render(request, 'edit_team.html', {'form':form, 'team': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_team(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =Team.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_team(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = TeamForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = TeamForm()
        return render(request, 'add_team.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_about(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = About.objects.get(pk=id)
            form = AboutForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = About.objects.get(pk=id)
            form =  AboutForm(instance=id)
            return render(request, 'edit_about.html', {'form':form, 'about': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_about(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =About.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_about(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AboutForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = AboutForm()
        return render(request, 'add_about.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_tech(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Tech.objects.get(pk=id)
            form = TechForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = Tech.objects.get(pk=id)
            form = TechForm(instance=id)
            return render(request, 'edit_tech.html', {'form':form, 'tech': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_tech(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =Tech.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_tech(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = TechForm(request.POST, request.FILES)    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = TechForm()
        return render(request, 'add_tech.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_person(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Person.objects.get(pk=id)
            form = PersonForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = Person.objects.get(pk=id)
            form = PersonForm(instance=id)
            return render(request, 'edit_person.html', {'form':form, 'person': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_person(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =Person.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_person(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = PersonForm()
        return render(request, 'add_person.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")



def edit_random(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            id = Random.objects.get(pk=id)
            form = RandomForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            id = Random.objects.get(pk=id)
            form = RandomForm(instance=id)
            return render(request, 'edit_random.html', {'form':form, 'random': id})
    else:
        return HttpResponse("You don't have access for this site....")


def delete_random(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi =Random.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return HttpResponse("You don't have access for this site....")



def add_random(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = RandomForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = RandomForm()
        return render(request, 'add_random.html', {'form' : form})

    else:
        return HttpResponse("You don't have access for this site....")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, '  Invalid Credintials')
            return redirect('login')
    else:
        return render(request, 'login.html')

# Accounts
def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email= email)
                user.save();
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
        return redirect('login')
    else:
        return render(request, 'login.html')

        
def logout(request):
    auth.logout(request)
    return redirect('/')

