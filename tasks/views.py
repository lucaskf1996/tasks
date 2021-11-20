from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.


def index(request):
    all_tasks = Task.objects.all()
    print(all_tasks)
    return HttpResponse(all_tasks)
