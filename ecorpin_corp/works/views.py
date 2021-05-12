from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import ClientReview

# Create your views here.

def projects_view(request):
    reviewList = ClientReview.objects.all()
    context = {
        'review_list' : reviewList,
    }
    #return HttpResponse("<h1>Ecorpin Secure Server - Projects </h1>")
    return render(request, 'works/index.html', context)