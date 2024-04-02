from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag
from todo.forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    form_class = TaskForm
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by(
            "is_done", "-datetime"
        )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("todo:task-details", kwargs={"pk": task.pk})
    )
