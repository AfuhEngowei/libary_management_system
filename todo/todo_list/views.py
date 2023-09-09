from django.shortcuts import render,redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Task


def home(request):
    return render(request,'todo_list/home.html')


def register(request):
    return render(request, 'todo_list/register.html')

def addtask(request):
        if request.method == "POST":
             title = request.POST ["title"]
             desciption  = request.POST ["description"]
             created_at = request.POST ["created_at"]
             completed = request.POST ["completed"]

        alltask = Task.objects.all().values()
        template = loader.get_template('todo_list/addtask.html')
        context = {
                'alltask':alltask
        }
        return HttpResponse(template.render(context,request))
def savetask(request):
    if request.method == "POST":
            title = request.POST ["title"]
            desciption  = request.POST ["description"]
            created_at = request.POST ["created_at"]
            completed = request.POST ["completed"]
            Task.objects.create(title=title, description=desciption,created_at=created_at,completed=True)
    savetask = Task.objects.all().values()
    template = loader.get_template('todo_list/savetask.html')
    context = {
                    'savetask':savetask
            }
    return HttpResponse(template.render(context,request))


def deletetask(request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        savetask = Task.objects.all().values()

        template = loader.get_template('todo_list/savetask.html')
        context = {
              'savetask':savetask
               }
        return HttpResponse(template.render(context,request))

       

def edittask(request, id):
        task = get_object_or_404(Task, id=id)
        if request.method == "PUT":
            title = request.PUT ["title"]
            desciption  = request.PUT ["description"]
            created_at = request.PUT ["created_at"]
            completed = request.PUT ["completed"]
            Task.objects.create(title=title, desciption=desciption, created_at=created_at)
        
        savetask = Task.objects.all().values()

        template = loader.get_template('todo_list/addtask.html')
        context = {
              'addtask':addtask 
               }
        return HttpResponse(template.render(context,request))

# Create your views here.
