from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('My response')


def group_posts(request, any_slug):
    return HttpResponse('My group response ' + any_slug)

# Create your views here.
