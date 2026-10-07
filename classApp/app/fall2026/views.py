from django.shortcuts import render, redirect
from .models import Task

# Define the method to visualize a task from the database
def task_list(request):
	task = Task.objects.all()

	return render(request, 
		'task/task_list.html',
		{'tasks':task}

		)

