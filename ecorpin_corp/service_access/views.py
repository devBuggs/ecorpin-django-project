from django.shortcuts import render, redirect
from django.views import View

from .models import ContactRequest
from .forms import ContactRequestForm

# Create your views here.

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

def service_logout(request):
    logout(request)
    return redirect(service_login_view)

class ServiceLoginView(View):
    template_name='service_access/service_login.html'
    def get(self, request):
        # <view logic>
        return render(request, 'service_access/service_login.html')

# Class Dashboard
class ServiceDashboardListView():
    #logic for the service dashboard of user
    pass

class ServiceUpdateView():
    # logic for the service/profile/information update request
    pass

class ServiceSupportView():
    #logic for the specific user support history with org. support
    pass

