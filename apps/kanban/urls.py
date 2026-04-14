from django.urls import path

from apps.kanban import views as kanban_views

app_name = "kanban"

urlpatterns = [
    path("", kanban_views.index, name="kanban_index"),
]
