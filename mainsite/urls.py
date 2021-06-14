from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('contact_us', views.contact_us, name='contact_us'),
    
    path('content', views.technology, name='technology'),
    path('technology', views.technology, name='technology'),
    path('personality', views.personality, name='personality'),
    path('random', views.random, name='random'),

    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),

    path('add_blog', views.add_blog, name='add_blog'),
    path('edit_blog/<int:id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),

    path('add_header', views.add_header, name='add_header'),
    path('edit_header/<int:id>/', views.edit_header, name='edit_header'),
    path('delete_header/<int:id>/', views.delete_header, name='delete_header'),

    path('add_about', views.add_about, name='add_about'),
    path('edit_about/<int:id>/', views.edit_about, name='edit_about'),
    path('delete_about/<int:id>/', views.delete_about, name='delete_about'),

    path('add_team', views.add_team, name='add_team'),
    path('edit_team/<int:id>/', views.edit_team, name='edit_team'),
    path('delete_team/<int:id>/', views.delete_team, name='delete_team'),

    path('add_tech', views.add_tech, name='add_tech'),
    path('edit_tech/<int:id>/', views.edit_tech, name='edit_tech'),
    path('delete_tech/<int:id>/', views.delete_tech, name='delete_tech'),

    path('add_person', views.add_person, name='add_person'),
    path('edit_person/<int:id>/', views.edit_person, name='edit_person'),
    path('delete_person/<int:id>/', views.delete_person, name='delete_person'),

    path('add_random', views.add_random, name='add_random'),
    path('edit_random/<int:id>/', views.edit_random, name='edit_random'),
    path('delete_random/<int:id>/', views.delete_random, name='delete_random'),

]
