from django.urls import path
from .views import (
    index,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TaskToggle,
    TagListView,
    TagCreate,
    TagUpdate,
    TagDelete,
)

urlpatterns = [
    path("", index, name="index"),
    path("create/", TaskCreate.as_view(), name="create-task"),
    path("task/<int:pk>/update/", TaskUpdate.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDelete.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", TaskToggle.as_view(), name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDelete.as_view(), name="tag-delete"),
]
