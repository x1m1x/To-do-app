from django.shortcuts import render
from django.views.generic import View

from .models import Action

def index(request):
    return render(request, 'to_do_list/main.html', context={'actions': Action.objects.order_by('-date')})


def add_action(request):
    response = request.POST.get('description')
    errors = ""
    if response != "":
        action = Action.objects.create(description=response)
    return render(request, 'to_do_list/main.html', context={'actions': Action.objects.order_by('-date')})


def delete_action(request):
    Action.objects.get(slug=request.POST.get('delete_action')).delete()
    return render(request, 'to_do_list/main.html', context={'actions': Action.objects.order_by('-date')})
