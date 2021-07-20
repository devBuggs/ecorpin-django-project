from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from ecorpin.models import EcorpinStat
from .models import ClientReview


# Create your views here.

def projects_view(request):
    reviewList = ClientReview.objects.all()
    stats = EcorpinStat.objects.get(pk=1)
    #logic for the recent works showcasing details with image...
    context = {
        'review_list' : reviewList,
        'stats' : stats,
    }
    #return response with data
    #return HttpResponse("<h1>Ecorpin Secure Server - Projects </h1>")
    return render(request, 'works/index.html', context)
