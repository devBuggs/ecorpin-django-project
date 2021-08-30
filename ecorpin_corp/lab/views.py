from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'lab/index.html', context=None)