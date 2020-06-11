from django.db import models
from django.shortcuts import reverse

from django.utils import timezone
import datetime
from time import time

def gen_slug(d):
    return d[::-1] + "-" + str(int(time()))

class Action(models.Model):
    date = models.DateTimeField("Время написания", auto_now_add=True)
    description = models.CharField("Действие", max_length=100)
    slug = models.SlugField("", max_length=100, default="slug")

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
