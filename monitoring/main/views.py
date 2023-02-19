from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm


def index(request):
    return redirect(voting)


def postuser(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    


def voting(request):
    userform = UserForm()
    return render(request, "voting.html", {"form": userform})

 
def results(request):
    return render(request, "results.html")


