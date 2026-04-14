from django.urls import path

from apps.workspace.views import home_view

app_name = "workspace"

urlpatterns = [
    path("", home_view, name="home"),
]
