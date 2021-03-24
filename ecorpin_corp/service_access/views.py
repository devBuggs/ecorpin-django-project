from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone

from .models import ContactRequest

from .forms import ContactRequestForm, ServiceAccessLoginForm

# Create your views here.
def main(request):
    form = ServiceAccessLoginForm()
    if request.method=="POST":
        if form.is_valid:
            #authenticate
            if next:
                return redirect(next)
            return redirect('/')
    else:
        form = ServiceAccessLoginForm()
    context = {
        'form' : form,
    }
    return HttpResponseRedirect('/')

def contact_request(request):
    serverMsg = ''
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            print("*******************************************************")
            serverMsg = "Contact Request is received. We'll contact you shortly. "
            return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
        else:
            print("-------------------------------------------------------")
    else:
        form = ContactRequestForm()
    context = { 'form': form, }
    return render(request, 'service_access/contact_request.html', context)