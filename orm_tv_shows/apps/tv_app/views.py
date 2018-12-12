from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Show

def index(request):

    return render(request, "tv_app/addshow.html")

def show_all(request):
    showz = {
        "shw":Show.objects.all()
    }
    print (showz["shw"][0])
    return render(request, "tv_app/index.html", showz)

def add_show(request):
    x = request.session['idd']
    content = Show.objects.get(id=x).__dict__
    print(content)

    return render(request, "tv_app/display.html", content)

def display(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST["release_date"])

    new_time = datetime.strptime(request.POST["release_date"], "%Y-%m-%d")
    print(new_time)
    Show.objects.create(title=request.POST["title"],network=request.POST["network"],release_date=request.POST["release_date"],description=request.POST["description"])
    request.session['idd'] = Show.objects.last().id
    print(Show.objects.last().id)
    return redirect("/add_show")

def add(request):

    return render(request, "tv_app/addshow.html")

def delete(request, my_val):
    d=Show.objects.get(id=my_val)
    d.delete()

    return redirect("/show_all ")

def reshow(request, my_val):
    x = my_val
    content = Show.objects.get(id=x).__dict__

    return render(request, "tv_app/display.html", content)

def edit(request, my_val):
    x = my_val
    content = Show.objects.get(id=x).__dict__

    return render(request, "tv_app/edit.html", content)

def redisplay(request, my_val):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST["release_date"])

    new_time = datetime.strptime(request.POST["release_date"], "%Y-%m-%d")
    c = Show.objects.get(id=my_val)
    #edituser = {"title":request.POST["title"],"network":request.POST["network"],"release_date":request.POST["release_date"],"description":request.POST["description"]}
    c.title = request.POST["title"]
    c.network = request.POST["network"]
    c.release_date = request.POST["release_date"]
    c.description = request.POST["description"]
    c.save
    request.session['idd'] = my_val
    return reshow("/add_show/my_val")
    
# Create your views here.
