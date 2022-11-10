from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


def index(request):
    if request.method == "POST":
        return HttpResponse(f"<h2>Привет, ВАЛЯ</h2>")
    else:
        userform = Registration()
        return render(request, "registration.html", {"form": userform})
