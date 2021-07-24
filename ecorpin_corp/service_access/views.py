from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 

from django.contrib.auth import authenticate, login, logout

from .models import ContactRequest, ServiceUser
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

def login_view(request):
    if request.method == 'POST':
        sid = request.POST.get('serviceId')
        pwd = request.POST.get('password')
        prefix = sid[:7]
        if str(prefix) == str("EC-56020"):
            print("Service Id Validation Done")
        else:
            print("Service Id Validation Failed!")
        service_user_obj = ServiceUser.objects.filter(service_id = sid)
        if service_user_obj is not None:
            print("-------------------> Service available for the request id")
            print("-------------------> ", service_user_obj)
            print("-------------------> ", service_user_obj[0].user.username)
            username = service_user_obj[0].user.username
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('service_access:dashboard')
            #login(request, username=username, password=pwd)
            return HttpResponse("Something went wrong in our server! #ecorpians ")
            #return redirect('service_access:dashboard')
        else:
            print("-------------------> No user found..")
    return render(request, 'service_access/service_login.html')

class ServiceDashboard(View):
    template_name='service_access/dashboard.html'
    def get(self, request):
        # <view logic>
        return render(request, 'service_access/dashboard.html')
    def post(self, request):
        #<view logic>
        return redirect('ecorpin:team')

class ServiceUpdateView():
    # logic for the service/profile/information update request
    pass

class ServiceSupportView():
    #logic for the specific user support history with org. support
    pass
