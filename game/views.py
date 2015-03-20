from django.shortcuts import render
from rpg.models import Room


def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)


def home2(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    template = "home2.html"
    return render(request, template, context)


def home3(request):
    context = {}
    template = "home3.html"
    return render(request, template, context)


def home4(request):
    context = {}
    template = "home4.html"
    return render(request, template, context)


def home5(request):
    context = {}
    template = "home5.html"
    return render(request, template, context)


def home6(request):
    context = {}
    template = "home6.html"
    return render(request, template, context)
