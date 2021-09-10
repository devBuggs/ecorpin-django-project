from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == "POST":
        data = dict(request.POST)
        print("----------> ", data)
        user_mail = data['user_email'][0]
        user_subject = data['user_subject'][0]
        user_message = data['user_message'][0]
        print("mail :: ", user_mail, "\nsubject :: ", user_subject, "\nmessage :: ", user_message)
        email_from = settings.EMAIL_HOST_USER
        recipitent_list = [user_mail, ]
        send_mail(user_subject, user_message, email_from, recipitent_list)
        return render(request, 'lab/index.html', {mail_response:'email send successfully...'})
        #return HttpResponseRedirect('index')
    else:
        return render(request, 'lab/index.html', context=None)
