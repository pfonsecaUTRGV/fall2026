from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm

# Define the method to visualize a task from the database


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


