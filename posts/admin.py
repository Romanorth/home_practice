from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filters = ('pub_date',)
    empty_value_display = '-empty-' 


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','slug',)
    search_fields = ('title',)
    list_filters = ('title',)
    empty_value_display = '-empty-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
