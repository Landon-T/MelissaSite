import json
import markdown2
import random
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from . import util


class NewPostForm(forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":25, "cols":100}))

# Create your views here.
def index(request):
    return render(request, 'mel_site/index.html')


def meet(request):
    return render(request, 'mel_site/meet_mel.html')

def speak(request):
    entry = util.get_entry("Speaking & Events")
    if entry != None:
        return render(request, 'mel_site/speak_events.html', {
            "content": markdown2.markdown(entry, extras=["footnotes"]), 
            "title": "Speaking & Events"
        })
    return render(request, 'mel_site/speak_events.html')

def involved(request):
    entry = util.get_entry("Get Involved")
    if entry != None:
        return render(request, 'mel_site/get_involved.html', {
            "content": markdown2.markdown(entry, extras=["footnotes"]), 
            "title": "Get Involved"
        })
    return render(request, 'mel_site/get_involved.html')

def store(request):
    return render(request, 'mel_site/store.html')



def create(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
        pages = util.list_entries
        if request.method == "POST":
            form = NewPostForm(request.POST)
            if form.is_valid():
                #Save the article
                util.save_entry(form.cleaned_data["title"], form.cleaned_data["body"])
                #return HttpResponseRedirect(reverse("wiki", args=[form.cleaned_data["title"]]))
                #return somthing new here
            else:
                # return the filled form if there is an error
                return render(request, "mel_site/create.html",{
                    "form": form,
                    "pages": pages,
                    "title": None
                })
        return render(request, "mel_site/create.html",{
            "form": NewPostForm(),
            "pages": pages,
            "title": None
        })
    
    else:
        #ask user to login
        return render(request, "mel_site/login.html")


def edit(request, title):
    pages = util.list_entries
    form = NewPostForm({'title':title, 'body': util.get_entry(title) })
    return render(request, "mel_site/create.html",{ 
        "form":form,
        "pages": pages,
        "title": title
    })




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mel_site/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "mel_site/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mel_site/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mel_site/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mel_site/register.html")

