from django.shortcuts import render


def home(request):
    context = {
        "title": "Employees Manager API",
    }
    return render(request, "home.html", context=context)
