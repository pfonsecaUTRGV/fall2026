import requests
import re

from django.shortcuts import render, redirect
from .models import Task, PokemonTeam, TeamPokemon
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
# Define the method to visualize a task from the database


def home(request):
    return render(request,"task/home.html")

def register(request): 
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)

			return redirect('dashboard')
	else: 
		form = UserCreationForm()

	return render(request, 'task/register.html', {'form':form})


def task_list(request):
	task = Task.objects.all()

	return render(request, 
		'task/task_list.html',
		{'tasks':task}

		)

def add_task(request):
	if request.method == 'POST':
		title = request.POST.get('title','').strip()
		date =  request.POST.get('date','').strip()
		if title:
			Task.objects.create(title=title, date = date)
			return redirect('task_list')

	return render(request,'task/add_task.html')

@login_required
def dashboard(request):
	return render(request,'task/dashboard.html')



@login_required
def pokemon_search(request):
    query = request.GET.get("q", "").strip().lower()
    pokemon = None

    if query:
        if not re.fullmatch(r"[a-z0-9-]+", query):
            messages.error(request, "Use a Pokémon name or positive ID.")
        else:
            try:
                response = requests.get(
                    f"https://pokeapi.co/api/v2/pokemon/{query}/",
                    timeout=10
                )
                if response.status_code == 404:
                    messages.error(request, "Pokémon not found.")
                else:
                    response.raise_for_status()
                    data = response.json()
                    pokemon = {
                        "id": data["id"],
                        "name": data["name"],
                        "image": data["sprites"]["front_default"],
                        "types": [
                            item["type"]["name"] for item in data["types"]
                        ],
                        "height": data["height"],
                        "weight": data["weight"],
                    }
            except (requests.RequestException, ValueError, KeyError):
                messages.error(request, "PokéAPI request failed.")

    teams = PokemonTeam.objects.filter(user=request.user)
    return render(request, "task/pokemon_search.html", {
        "query": query, "pokemon": pokemon, "teams": teams
    })

@login_required
def my_teams(request):
    teams = PokemonTeam.objects.filter(
        user=request.user
    ).prefetch_related("members")
    return render(request, "task/my_teams.html", {"teams": teams})


@login_required
@require_POST
def create_team(request):
    name = request.POST.get("name", "").strip()
    if not name or len(name) > 100:
        messages.error(request, "Enter a team name (1–100 characters).")
    else:
        PokemonTeam.objects.create(user=request.user, name=name)
        messages.success(request, "Team created.")
    return redirect("my_teams")















