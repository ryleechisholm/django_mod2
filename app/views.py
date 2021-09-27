from django.shortcuts import render
from django.http import HttpRequest
from app.teams_info import Team, TEAMS

def all_teams(request: HttpRequest):
    return render(request, "teams.html")


def which_team(request: HttpRequest, title: str):
    for team in TEAMS:
        if title == team.title:
            return render(request, "team.html", {"name": team.name, "team_info": team.info, "members": team.members})
