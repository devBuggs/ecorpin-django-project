from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.utils import timezone

from .models import spotlight, endpoint_info, ecorpian, feedback

from .forms import feedback_form

# Create your views here.
def fevicon_ecorpin(request):
    pass

def index_ecorpin(request):
    spotlightData = spotlight.objects.all().latest('spotlight_date')
    context = {
        'latest_spotlight': spotlightData,
    }
    return render(request, 'ecorpin/index.html', context)

def privacy(request):
    info = endpoint_info.objects.get(end_point="Privacy Policy")
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/privacy.html', context)

def team(request):
    info = endpoint_info.objects.get(end_point="Team")
    ecorpians = list(ecorpian.objects.all().order_by('joinDate'))
    context = {
        'info':info,
        'ecorpians_list':ecorpians,
    }
    return render(request, 'ecorpin/team.html', context)

def tou(request):
    info = endpoint_info.objects.get(end_point="Terms of Use")
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/tou.html', context)

def contact(request):
    info = endpoint_info.objects.get(end_point="Contact")
    #Content Query
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/contact.html', context)

def careers(request):
    info = endpoint_info.objects.get(end_point='Careers')
    #Content Query
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/careers.html', context)

def about(request):
    info = endpoint_info.objects.get(end_point='About')
    #Content Query
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/about.html', context)

def maintenance(request):
    info = endpoint_info.objects.get(end_point='Server Maintenance')
    #Content Query
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/maintenance.html', context)

def covid(request):
    info = endpoint_info.objects.get(end_point='Ecorpin Covid-19 Response')
    context = {
        'info':info,
    }
    return render(request, 'ecorpin/covid.html', context)

def feedback_create(request):
    serverMsg = ''
    info = endpoint_info.objects.get(end_point='Feedback')
    if request.method == 'POST':
        form = feedback_form(request.POST)
        if form.is_valid():
            form.save()
            print("*******************************************************")
            return HttpResponseRedirect('/')
        else:
            print("-------------------------------------------------------")
    else:
        form = feedback_form()
    context = {
        'form': form,
        'info': info,
        }
    return render(request, 'ecorpin/feedback.html', context)

def service(request):
    return HttpResponse("<h1>Ecorpin Secure Server - Services</h1>")
