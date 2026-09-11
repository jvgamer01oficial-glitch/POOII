from django.http import HttpResponse
from django.shortcuts import render

from Projeto1app.models import tarefa


# Create your views here.

def home(request):
    return render(request, "Projeto1app/home.html")

def tarefa_listar(request):
    tarefas = tarefa.objects.all()
    return render(request, "Projeto1app/tarefa_listas.html", {"tarefas" : tarefas})
