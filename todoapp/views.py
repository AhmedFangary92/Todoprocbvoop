from django.http import request, response
from django.http.response import HttpResponse, HttpResponseBase, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from .models import *
import datetime
from django.urls import reverse_lazy
# Create your views here.

class index(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todolist'


# def index(request):
#     return render(request, 'index.html')


class list(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todolist'


# def list(request):
#     mydectionary = {
#         'todolist' : Todo.objects.all()
#     }
#     return render(request, 'list.html', context=mydectionary)

class submit(View):
    
    def post(self, request):
        Todo(title=request.POST['title'], description=request.POST['description'],
         priority=request.POST['priority']).save()
        return HttpResponseRedirect('list')

# def submit(request):
#     obj = Todo()
#     obj.title = request.GET['title']
#     obj.description = request.GET['description']
#     obj.priority = request.GET['priority']
#     obj.save()
#     mydectionary = {
#         'todolist' : Todo.objects.all()
#     }
#     return render(request, 'list.html', context=mydectionary)

class delete(DeleteView):
    pk_url_kwarg = "pk"
    model = Todo
    success_url = '/list'
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=self.kwargs[self.pk_url_kwarg])
        todo.delete()
        return HttpResponseRedirect(self.success_url)


# def delete(request, id):
#     obj = Todo.objects.get(id=id)
#     obj.delete()
#     mydectionary = {
#         'todolist' : Todo.objects.all()
#     }

#     return render(request, 'list.html', context=mydectionary)

# class edit(ListView):
#     pk_url_kwarg = "pk"
#     model = Todo
#     template_name = 'edit.html'
#     success_url = 'list.html'
#     def edit(self, request, *args, **kwargs):
#         todo = get_object_or_404(Todo, pk=self.kwargs[self.pk_url_kwarg])
#         todo.save()
#         return HttpResponseBase(self.success_url)


def edit(request, id):
    obj = Todo.objects.get(id=id)
    mydectionary = {
        'id' : obj.id,
        'title' : obj.title,
        'description' : obj.description,
        'priority' : obj.priority
    }

    return render(request, 'edit.html', context=mydectionary)

class sortdata(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todolist'

    ordering = ['priority']

# def sortdata(request):
#     mydectionary = {
#         'todolist' : Todo.objects.all().order_by('priority')
#     }

#     return render(request, 'list.html', context=mydectionary)

class searchdata(ListView):
    template_name = 'list.html'
    model = Todo

    def get_queryset(self, *args, **kwargs):
        title = self.kwargs.get('title', 'list.html')
        object_list = self.model.objects.all()
        if title:
            object_list = object_list.filter(title__icontains=title)
            return object_list

# def searchdata(request):
#     q = request.GET['query']
#     mydictionary = {
#         'todolist' : Todo.objects.filter(title__contains=q)
#     }
#     return render(request,'list.html',context=mydictionary)

def update(request, id):
    
    updated_at = datetime.datetime.now()
    
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.created_at = updated_at
    obj.save()

    mydectionary = {
        'todolist' : Todo.objects.all()
    }
    return render(request, 'list.html', context=mydectionary)