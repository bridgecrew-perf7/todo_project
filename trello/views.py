from django.shortcuts import render, redirect
from .models import Task, TaskList
from .forms import TaskListForm, TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    task_list = TaskList.objects.all()
    return render(request, "trello/index.html", {'tasks': tasks, 'task_list': task_list})


def add_task_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at)
        task_list.save()
        return redirect('index')
    return render(request, 'trello/add_task_list.html', )


def add_task_list_2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('index')
    else:
        form = TaskListForm()
    return render(request, 'trello/add_task_list_2.html', {'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'trello/add_task.html', {'form': form})
