from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def projects_view(request):
    #return HttpResponse("<h1>Ecorpin Secure Server - Projects </h1>")
    return render(request, 'works/index.html', context=None)