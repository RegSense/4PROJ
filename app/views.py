from django.shortcuts import render
from django.http import HttpResponse
from app import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    # person = Person.objects.filter(first_name = 'Nom')[0]
    return render(request, 'login.html', locals())

def home(request):
    return render(request, 'home.html', locals())

def cours_eleve(request):
    person = "Retour base de données: " + User.objects.get(username='Abigail Byfford').first_name
    return render(request, 'cours_eleve.html', locals())

def administration(request):
    person = "Retour base de données: " + User.objects.get(username='Abigail Byfford').first_name
    obj_user = User.objects.all()
    user_dic = {
        "first_name": obj_user
    }
    allfirstname = User.objects.all().values_list('first_name', flat=True)
    alllastname = User.objects.all().values_list('last_name', flat=True)
    allemail = User.objects.all().values_list('email', flat=True)
    return render(request, 'administration.html', locals())