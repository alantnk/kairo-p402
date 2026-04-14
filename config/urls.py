"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/work/", permanent=False)),
    path("backend/", admin.site.urls),
    path(
        "session/",
        include(("django.contrib.auth.urls", "auth"), namespace="session"),
    ),
    path("work/", include("apps.workspace.urls")),
    path("kanban/", include("apps.kanban.urls")),
]

admin.AdminSite.site_header = "Backend Site"
admin.AdminSite.site_title = "🔐"
admin.AdminSite.index_title = "Staff-Only Zone"
