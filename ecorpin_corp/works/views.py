from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from ecorpin.models import EcorpinStat
from .models import ClientReview


# Create your views here.

def projects_view(request):
    reviewList = ClientReview.objects.all()
    stats = EcorpinStat.objects.get(pk=1)
    context = {
        'review_list' : reviewList,
        'stats' : stats,
    }
    #return HttpResponse("<h1>Ecorpin Secure Server - Projects </h1>")
    return render(request, 'works/index.html', context)