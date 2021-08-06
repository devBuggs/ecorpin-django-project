from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from service_access.models import ContactRequest, ServiceUser, Service
from ecorpin.models import Endpoint_info
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

@login_required(login_url='service_access:login')
def service_logout(request):
    logout(request)
    return redirect("service_access:login")

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
                print("Logging in user")
                return redirect('service_access:dashboard')
            return HttpResponse("Something went wrong in our server! #ecorpians ")
        else:
            print("-------------------> No user found..")
    return render(request, 'service_access/service_login.html')

class ServiceDashboard(LoginRequiredMixin, View):
    template_name='service_access/dashboard.html'
    def get(self, request):
        # <view logic>
        print("-------------------------------------------------- getting things : dashboard ")
        #projects = Service.objects.get(service_id = request.user.service_user.service_id.id)
        service_user_id = ServiceUser.objects.get(user = request.user.id)
        #print("----------------------------------> ", request.user)
        service_list = Service.objects.filter(service_id = service_user_id)
        print("-----------------------------------> ", service_list)
        #print("-----------------------------------> ", projects)
        info = Endpoint_info.objects.get(end_point="Dashboard")
        context = {
            'service_list': service_list,
            'info':info,
        }
        return render(request, 'service_access/dashboard.html', context)
    def post(self, request):
        #<view logic>
        return redirect('ecorpin:feedback')

class ServiceUserProfile(LoginRequiredMixin, View):
    template_name = 'service_access/profile.html'
    
    def get(self, request):
        #return reverse('ecorpin:team')
        print("--------------------------- Service User Profile ---------------------------")
        info = Endpoint_info.objects.get(end_point="Profile")
        context = {
            'info':info,
        }
        return render(request, 'service_access/profile.html', context)

    def post(self, request):
        pass

class ServiceUpdateView():
    # logic for the service/profile/information update request
    pass

class ServiceSupportView():
    #logic for the specific user support history with org. support
    pass
