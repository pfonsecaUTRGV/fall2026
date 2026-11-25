from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.task_list, name ='task_list'),
	path('add_task/',views.add_task, name ='add_task'),
	path("teams/", views.my_teams, name="my_teams"),
	#Pokemon trainer team MVP urls
	path('register/',views.register, name='register'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('login/',auth_views.LoginView.as_view(
		template_name='task/login.html'),name='login'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path("pokemon_search/", views.pokemon_search, name="pokemon_search"),
	path("teams/create/",views.create_team,name="create_team"),
]