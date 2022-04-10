from django.shortcuts import render, HttpResponse, get_object_or_404

from . models import Post, Group


TEMPLATES = {
    'index': 'posts/index.html',
    'group_list': 'posts/group_list.html',
}


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, TEMPLATES['index'], context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, TEMPLATES['group_list'], context)

# Create your views here.
