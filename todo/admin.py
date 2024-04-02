from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime", "deadline", "is_done")
    list_filter = ("datetime", "deadline", "is_done")
    search_fields = ("title", "content")
    date_hierarchy = "datetime"
    ordering = ("-datetime",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
