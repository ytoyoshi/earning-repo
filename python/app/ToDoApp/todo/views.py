from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView
from django.views import generic
from .models import TodoModel
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.shortcuts import redirect
from . import models,forms
from .forms import TodoForm

# Create your views here.

class TodoList(ListView):
    template_name = 'TodoList.html'
    queryset = models.TodoModel.objects.filter(complete=TodoModel.CompleteType.INCOMPLETE)

class DetailList(UpdateView):
    template_name = 'detail.html'
    model = TodoModel
    form_class = TodoForm
    success_url = reverse_lazy('list')

class CreateList(CreateView):
    template_name = 'create.html'
    model = TodoModel
    form_class = TodoForm
    success_url = reverse_lazy('list')

@require_POST
def Complete(request,id):
    todoModel = get_object_or_404(TodoModel,id=id)
    todoModel.complete = TodoModel.CompleteType.COMPLETE
    todoModel.save()
    return redirect("list")