from django.contrib import admin
from django.urls import path

from app.views import all_teams, management, community, procurement, documentation

urlpatterns = [
    path('', all_teams),
    path('management/', management),
    path('procurement/', procurement),
    path('documentation/', documentation),
    path('community/', community),
]
