from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from .models import Person


def index(request):
    return render(request, "index.html")


def postuser(request):
    name = request.POST.get("fio")
    age = int(request.POST.get("age"))
    vote = int(request.POST.get("radioButton"))

    new_vote = Person.objects.create(name=name, age=age, vote=vote)

    return redirect(results)


def voting(request):
    userform = UserForm()
    return render(request, "voting.html", {"form": userform})


def results(request):
    data = Person.objects.all()

    bmw_count = data.filter(vote="1").count()
    print(bmw_count)

    mercedes_count = data.filter(vote="2").count()
    print(mercedes_count)

    audi_count = data.filter(vote="3").count()
    print(audi_count)

    return render(
        request,
        "results.html",
        {
            "data": data,
            "bmw_count": bmw_count,
            "mercedes_count": mercedes_count,
            "audi_count": audi_count,
        },
    )
