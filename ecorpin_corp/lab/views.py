from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        print("----------> ", data)
    else:
        context = {
            'footer' : False,
            "layout" : True
        }
        return render(request, 'lab/index.html', context=None)
