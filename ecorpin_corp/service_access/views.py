from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.core.mail import send_mail


from service_access.models import ContactRequest, ServiceUser, Service
from ecorpin.models import Endpoint_info
from .forms import ContactRequestForm
from payment.models import Transaction

# Create your views here.
def contact_request(request):
    serverMsg = ''
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            serverMsg = "Contact Request is received. We'll contact you shortly. "
            #return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
            return render(request, 'service_access/new_project.html', { 'data':serverMsg })
        else:
            print("--------> SOMETHING WENT WRONG.")
            serverMsg = "Something went wrong! please try again... "
            #return render(request, 'service_access/contact_request.html', { 'data':serverMsg })
            return render(request, 'service_access/new_project.html', { 'data':serverMsg })
    else:
        form = ContactRequestForm()
        context = { 'form': form, }
        #return render(request, 'service_access/contact_request.html', context)
        return render(request, 'service_access/new_project.html', context)

@login_required
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
        service_user_id = ServiceUser.objects.get(user = request.user.id)
        service_list = Service.objects.filter(service_id = service_user_id)
        payment_list = Transaction.objects.filter(user=request.user)
        info = Endpoint_info.objects.get(end_point="Dashboard")
        context = {
            'payment_list': payment_list,
            'service_list': service_list,
            'info':info,
        }
        return render(request, 'service_access/dashboard.html', context)
    def post(self, request):
        #<view logic>
        user = request.user
        data = request.POST
        service_user_id = ServiceUser.objects.get(user = request.user.id)
        service_list = Service.objects.filter(service_id = service_user_id)
        payment_list = Transaction.objects.filter(user=request.user)
        info = Endpoint_info.objects.get(end_point="Dashboard")
        #print('----------------> ', data)
        user_mail = request.user.email
        user_subject = str(data['catogary'] +" | "+user.first_name+' '+user.last_name + " | "+ data['phone'] + " | Service Access")
        #print('----------------> ', user_subject)
        user_message = data['message']
        #print('----------------> ', user_message)
        print("mail :: ", user_mail, "\nsubject :: ", user_subject, "\nmessage :: ", user_message)
        email_from = settings.EMAIL_HOST_USER
        recipitent_list = [user_mail, ]
        send_mail(user_subject, user_message, email_from, recipitent_list)
        context = {
            'payment_list': payment_list,
            'service_list': service_list,
            'info':info,
            'mail_response': 'response submitted! thank you..'
        }
        return render(request, 'service_access/dashboard.html', context)
        
class ServiceUserProfile(LoginRequiredMixin, View):
    template_name = 'service_access/profile.html'

    def get(self, request):
        #return reverse('ecorpin:team')
        #print("--------------------------- Service User Profile ---------------------------")
        info = Endpoint_info.objects.get(end_point="Profile")
        context = {
            'info':info,
        }
        return render(request, 'service_access/profile.html', context)

    def post(self, request):
        # logic for service user profile post method
        pass

class ServiceUpdateView():
    # logic for the service/profile/information update request
    def get(self, request):
        # login for service update get method
        pass

    def post(self, request):
        # login for service update get method
        pass

    pass

class ServiceSupportView():
    #logic for the specific user support history with org. support
    pass
