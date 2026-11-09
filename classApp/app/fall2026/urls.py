from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.task_list, name ='task_list'),
	path('add_task/',views.add_task, name ='add_task'),

	#Pokemon trainer team MVP urls
	path('register/',views.register, name='register'),

	path('login/',auth_views.LoginView.as_view(
		template_name='tasks/login.html'),name='login'),
	path('dashboard/',views.dashboard,name='dashboard'),
]