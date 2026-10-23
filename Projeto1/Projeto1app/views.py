from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from Projeto1app.models import tarefa


# Create your views here.

def home(request):
    return render(request, "Projeto1app/home.html")

class TarefaLisView(ListView):
    model = tarefa

class TarefaCreateView (CreateView):
    model = tarefa
    fields = ["titulo", "prazoLimite",
              "terminado_em", "pessoa_responsavel"]
    success_url = reverse_lazy("tarefa_list")

class TarefaUpdateView (UpdateView):
    model = tarefa
    fields = ["titulo", "prazoLimite",
              "terminado_em", "pessoa_responsavel"]
    success_url = reverse_lazy("tarefa_list")

class TarefaDeleteView (DeleteView):
    model = tarefa
    success_url = reverse_lazy("tarefa_list")