from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from .forms import CreateNewTaskForm, CreateNewProjectForm


# Create your views here.

def index(request):
    title = 'Django App!!!!'
    return render(request, 'index.html',{
        'title': title
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s!</h2>" %username)


def about(request):
    username = 'kenny'
    return render(request, 'about.html',{
        'username': username
    })

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #task =  Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = list(Task.objects.values())
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTaskForm()   
        })
    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        print(title)
        print(description)
        Task.objects.create(title=title, description=description, 
                            project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProjectForm()
        })
    elif request.method == 'POST':
        name = request.POST['name']
        
        print(name)
        Project.objects.create(name=name)
        return redirect('projects')


def project_detail(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    
    return render(request, 'project_detail.html', {
        'project': project,
        'tasks': tasks
    })