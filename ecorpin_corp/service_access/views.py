from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import ContactRequest
from .forms import ContactRequestForm

# Create your views here.

def service_access_view(request):
    #service access backend
    #return HttpResponse('<h1>Ecorpin Secure Server - Service Access</h1>')
    return render(request, 'service_access/serviceLogin.html', context=None)

def contact_request(request):
    serverMsg = ''
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            serverMsg = "Contact Request is received. We'll contact you shortly. "
            return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
        else:
            print("--------> SOMETHING WENT WRONG.")
            serverMsg = "Something went wrong! please try again... "
            return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
    else:
        form = ContactRequestForm()
        context = { 'form': form, }
        return render(request, 'service_access/contact_request.html', context)

def service_login_view(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        login_data = request.POST
        if login_data['email'] != '' and login_data['password'] != '':
            service_id = login_data['email']
            password = login_data['password']
            user = authenticate(username=service_id, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect(ServiceDashboardView)
    return render(request, 'service_access/serviceLogin.html')

class ServiceDashboardView(TemplateView):
    template_name = 'service_access/dashboard.html'
    #model = ServiceDashboard

def service_logout_view():
    logout(request)
    return redirect(service_login_view)