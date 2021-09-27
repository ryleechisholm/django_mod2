from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.all_teams, name="opening"),
    path('<str:title>/', views.which_team, name="t_template")
]
