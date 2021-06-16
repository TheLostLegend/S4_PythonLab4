from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
