from django.shortcuts import render, redirect
from menu.models import MenuItem


def draw_menu(request, menu_url):
    return render(request, 'menu/menu.html', {'menu_url': menu_url})

def index(request):
    return render(request, 'menu/menu.html', {'menu_url': "main_menu"})