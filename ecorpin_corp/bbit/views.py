from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index_bbit(request):
    #return HttpResponse("<h1>Ecorpin Secure Server - Block-Bit</h1>")
    return render(request, 'bbit/index.html', context=None)
