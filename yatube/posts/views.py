from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = "posts/index.html"
    text = 'Эта главная страница проекта Yatube'
    contex = {
        'text': text,
    }
    return render(request, template, contex)


def group_posts(request):
    template = "posts/group_list.html"
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'text': text,
    }
    return render(request, template, context)