from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from Todo.forms import TaskCreateForm
from Todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-datetime")
    context = {"tasks": tasks}
    return render(request, "index.html", context=context)


class TaskCreate(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("index")


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("index")


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TaskToggle(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("index")


class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreate(CreateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagUpdate(UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
