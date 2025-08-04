from django.shortcuts import render
from .models import agenda
from datetime import date

def index(request):
    tarefas = agenda.objects.all()
    context = {
        'tarefas': tarefas,
        'hoje': date.today(), 
    } 
    return render(request, 'app/index.html', context) 