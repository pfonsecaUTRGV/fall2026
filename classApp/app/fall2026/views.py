from django.shortcuts import render, redirect
from .models import Task

# Define the method to visualize a task from the database
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


