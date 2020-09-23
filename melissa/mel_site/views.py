from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import random
from . import util


class NewPostForm(forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":50}))

# Create your views here.
def index(request):
    return render(request, 'mel_site/index.html')


def meet(request):
    return render(request, 'mel_site/meet_mel.html')

def speak(request):
    entry = util.get_entry("Speaking & Events")
    if entry != None:
        return render(request, 'mel_site/speak_events.html', {
            "content": markdown2.markdown(entry), 
            "title": "Speaking & Events"
        })
    return render(request, 'mel_site/speak_events.html')

def involved(request):
    entry = util.get_entry("Get Involved")
    if entry != None:
        return render(request, 'mel_site/get_involved.html', {
            "content": markdown2.markdown(entry), 
            "title": "Get Involved"
        })
    return render(request, 'mel_site/get_involved.html')

def store(request):
    return render(request, 'mel_site/store.html')

def create(request):

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
                "form": form
            })
    return render(request, "mel_site/create.html",{
        "form": NewPostForm()
    })

def edit(request, title):
    form = NewArticleForm({'title':title, 'body': util.get_entry(title) })
    return render(request, "mel_site/create.html",{ 
        "form":form
    })