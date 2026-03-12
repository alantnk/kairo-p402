from django.urls import path

from work_project.views import home_view

app_name = "work_project"

urlpatterns = [
    path("", home_view, name="home"),
]
