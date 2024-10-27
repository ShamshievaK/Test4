from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from tasks.models import Task


def mane_page_view(request):
    return render(request, 'base.html')

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail_view(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')

