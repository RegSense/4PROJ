from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cours_eleve/', views.cours_eleve, name='cours_eleve'),
]