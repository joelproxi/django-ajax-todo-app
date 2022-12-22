import json

from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods 
from django.views.generic import View

from .models import Task

# Create your views here.


def index(request, template=None):
    tasks = Task.objects.all()
    template = 'todo/list.html'
    return render(request=request,
                  template_name=template)
    
    
def get_task(request):
    tasks = Task.objects.all()
    template = 'todo/ajax_task_list.html'
    return render(request=request,
                  template_name=template, 
                  context={'tasks': tasks})
    


@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def add_task(request):
    data = json.loads(request.body)
    
    if request.method == 'POST':
        print('post')
        Task.objects.create(description=data['des'])
        return JsonResponse({'status': 'success'})

    if request.method == 'PUT':
        print('put')
        print(data)
        Task.objects.filter(id=data["id"])\
            .update(
                description=data["des"], 
                completed=data["com"])
        return JsonResponse({'status': 'success'})
    
    if request.method == 'DELETE':
        Task.objects.filter(id=data["id"]).delete()
    return JsonResponse({'status': 'error'})


