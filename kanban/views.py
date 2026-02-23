from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers


@vary_on_headers("HX-Request")
def index(request):
    if request.htmx:
        return render(request, "kanban/htmx/partial.html")
    return render(request, "kanban/base.html")
