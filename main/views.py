import random
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cafe
from .forms import CafeForm


def index(request):
    #cafes = Cafe.objects.order_by('-id')[:2 ]
    cafes = Cafe.objects.all()
    #cafes = Cafe.objects.filter(id__gt=20)
    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'cafes': cafes})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = CafeForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def cafe_view(request, id=1):
    cafe = Cafe.objects.get(id=id)
    return render(request, 'main/cafe_view.html', {'title': 'Обраний заклад', 'cafe': cafe})

def index_tab(request):
    cafes = Cafe.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'Перелік закладів', 'cafes': cafes})


def cafe_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CafeForm()
        else:
            cafe = Cafe.objects.get(id=id)
            form = CafeForm(instance=cafe)
        return render(request, 'main/cafe_edit.html', {'form': form})
    else:
        if id == 0:
            form = CafeForm(request.POST)
        else:
            cafe = Cafe.objects.get(id=id)
            form = CafeForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
        return redirect('main')


def cafe_delete(request, id=0):
    cafe = Cafe.objects.get(id=id)
    cafe.delete()
    cafes = Cafe.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'Перелік закладів', 'cafes': cafes})

def picture(request):
    return render(request, 'main/main.html')


