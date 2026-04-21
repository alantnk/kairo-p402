from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ("cod", "title", "assigned_to", "due_date", "created_at")
    list_filter = ("assigned_to", "due_date", "created_at")
    search_fields = ("title", "description", "cod")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Card, CardAdmin)
