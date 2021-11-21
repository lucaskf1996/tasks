from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

# Create your views here.


def index(request):
    all_tasks = Task.objects.all()
    return JsonResponse(all_tasks, safe=False)
