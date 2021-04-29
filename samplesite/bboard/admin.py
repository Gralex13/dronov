from django.contrib import admin

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class RubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubAdmin)

