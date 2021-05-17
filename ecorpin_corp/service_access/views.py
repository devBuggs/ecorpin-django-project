from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone

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
