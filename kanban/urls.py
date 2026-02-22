from django.urls import path

from . import views as kanban_views

urlpatterns = [
    path("", kanban_views.index, name="kanban_index"),
]
