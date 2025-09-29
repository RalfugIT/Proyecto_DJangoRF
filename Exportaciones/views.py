from django.shortcuts import render, get_object_or_404, redirect
from .models import Embarque, Operacion

def home(request):
    embarques = Embarque.objects.all()
    return render(request, 'home.html', {'embarques': embarques})

def create_view(request):
    return render(request, 'create.html')