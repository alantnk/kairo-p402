# flake8: noqa: E501
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from nanoid import generate
from taggit.managers import TaggableManager

User = get_user_model()


def generate_code():
    return generate(size=6)


class DateTimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Card(DateTimeStampedModel):
    cod = models.CharField(unique=True, default=generate_code, max_length=21)
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique_for_date="created_at", max_length=255, blank=True)

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.cod}) - {self.title}"
