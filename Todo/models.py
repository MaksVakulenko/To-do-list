from django.db import models
from django.forms import CharField


class Task(models.Model):
    content = CharField(max_length=255),
    datetime = models.DateTimeField(auto_now_add=True),
    deadline = models.DateTimeField(),
    is_done = models.BooleanField(default=False),
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.content

class Tag(models.Model):
    name = CharField(max_length=255)
