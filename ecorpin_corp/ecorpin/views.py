from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.utils import timezone

from .models import Spotlight, Endpoint_info, Ecorpian, Feedback

from .forms import FeedbackForm

# Create your views here.
def fevicon_ecorpin(request):
    pass

def index_ecorpin(request):
    spotlightData = Spotlight.objects.all().latest('spotlight_date')
    context = {
        'latest_spotlight': spotlightData,
    }
    return render(request, 'ecorpin/index.html', context)

def privacy(request):
    info = Endpoint_info.objects.get(end_point="Privacy Policy")
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/privacy.html', context)

def team(request):
    info = Endpoint_info.objects.get(end_point="Team")
    ecorpians = list(Ecorpian.objects.all().order_by('joinDate'))
    context = {
        'info':info,
        'ecorpians_list':ecorpians,
    }
    return render(request, 'ecorpin/team.html', context)

def tou(request):
    info = Endpoint_info.objects.get(end_point="Terms of Use")
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/tou.html', context)

def contact(request):
    info = Endpoint_info.objects.get(end_point="Contact")
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/contact.html', context)

def careers(request):
    info = Endpoint_info.objects.get(end_point='Careers')
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/careers.html', context)

def about(request):
    info = Endpoint_info.objects.get(end_point='About')
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/about.html', context)

def maintenance(request):
    info = Endpoint_info.objects.get(end_point='Server Maintenance')
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/maintenance.html', context)

def covid(request):
    info = Endpoint_info.objects.get(end_point='Ecorpin Covid-19 Response')
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/covid.html', context)

def feedback_create(request):
    serverMsg = ''
    info = Endpoint_info.objects.get(end_point='Feedback')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("*******************************************************")
            return HttpResponseRedirect('/')
        else:
            print("-------------------------------------------------------")
    else:
        form = FeedbackForm()
    context = {
        'form': form,
        'info': info,
        }
    return render(request, 'ecorpin/feedback.html', context)

def service(request):
    return HttpResponse("<h1>Ecorpin Secure Server - Services</h1>")
