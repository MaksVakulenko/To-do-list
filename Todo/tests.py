from django.test import TestCase, Client
from django.urls import reverse
from .models import Task, Tag
from datetime import datetime


class TaskCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Task", deadline=datetime.now(), is_done=False
        )
        self.task.tags.add(self.tag)

    def test_task_create(self):
        response = self.client.post(
            reverse("create-task"),
            {
                "content": "New Task",
                "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M"),
                "tags": [self.tag.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_update(self):
        response = self.client.post(
            reverse("task-update", kwargs={"pk": self.task.pk}),
            {
                "content": "Updated Task",
                "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M"),
                "tags": [self.tag.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")

    def test_task_delete(self):
        response = self.client.get(reverse("task-delete", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())


class TagCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_create(self):
        response = self.client.post(reverse("tag-create"), {"name": "New Tag"})
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_tag_update(self):
        response = self.client.post(
            reverse("tag-update", kwargs={"pk": self.tag.pk}), {"name": "Updated Tag"}
        )
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")

    def test_tag_delete(self):
        response = self.client.get(reverse("tag-delete", kwargs={"pk": self.tag.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())
