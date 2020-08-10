from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mel_site/index.html')


def meet(request):
    return render(request, 'mel_site/meet_mel.html')