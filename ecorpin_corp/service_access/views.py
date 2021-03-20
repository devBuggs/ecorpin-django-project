from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone

from .models import ContactRequest

from .forms import ContactRequestForm

# Create your views here.
def main(request):
    return HttpResponseRedirect('/team')

def contact_request(request):
    serverMsg = ''
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            print("*******************************************************")
            serverMsg = 'Data recived.. #ecorpin'
            return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
        else:
            print("-------------------------------------------------------")
    else:
        form = ContactRequestForm()
    context = { 'form': form, }
    return render(request, 'service_access/contact_request.html', context)