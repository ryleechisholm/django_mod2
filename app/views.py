from django.shortcuts import render
from django.http import HttpRequest

def all_teams(request: HttpRequest):
    return render(request, "teams.html")

def management(request: HttpRequest):
    return render(request, "manage.html")
    
def procurement(request: HttpRequest):
    return render(request, "procure.html")

def documentation(request: HttpRequest):
    return render(request, "document.html")

def community(request: HttpRequest):
    return render(request, "commune.html")