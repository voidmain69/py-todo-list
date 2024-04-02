from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TaskDetailView,
    TaskCompleteView,
)

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/<int:pk>/complete/",
        TaskCompleteView.as_view(),
        name="task-complete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "task/<int:pk>/details/", TaskDetailView.as_view(), name="task-details"
    ),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
