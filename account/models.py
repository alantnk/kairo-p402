# flake8: noqa: E501
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Account(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    role = models.ForeignKey("account.Role", on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        email_exists = User.objects.filter(email=self.user.email).exists()

        if email_exists and self.user.pk is None:
            raise ValueError("A user with this email already exists.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Account - {self.user.username}"


class Role(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
