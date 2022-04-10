from django.urls import path, include

from . import  views

app_name = 'posts'
group_patterns = ([
    path('<str:slug>/', views.group_posts, name='group'),
], 'group')

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', include(group_patterns, namespace='group_url')),
]
