from django.shortcuts import render, HttpResponse


TEMPLATES = {
    'index': 'templates/posts/index.html',
}


def index(request):
    return render(request, TEMPLATES['index'])


def group_posts(request, any_slug):
    return HttpResponse('My group response ' + any_slug)

# Create your views here.
