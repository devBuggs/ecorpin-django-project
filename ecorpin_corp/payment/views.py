from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings

# importing models
from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from service_access.models import Service

# import other apps views
#from service_access.views import ServiceUserProfile

# Create your views here.
@login_required
def initiate_payment(request):
    if request.method == 'GET':
        current_user = request.user
        service_id = request.user.service_user.service_id
        orderAmount = '5000'
        orderCurrency = 'INR'
        orderNote = 'Ecorpin Corporation payment for "{username}" having Service ID {sid}'.format(username=current_user.username, sid=service_id)
        customerName = current_user.first_name +' '+current_user.last_name
        customerEmail = current_user.email
        customerPhone = current_user.service_user.projects
        postData = {
            "orderAmount":orderAmount,
            "orderCurrency":orderCurrency,
            "orderNote":orderNote,
            "customerName":customerName,
            "customerPhone":customerPhone,
            "customerEmail":customerEmail
        }
        context = {
            'payment':postData
        }
        return render(request, 'payment/pay.html', context)
    try:
        amount = int(request.POST['amount'])
        user = request.user
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)
    except:
        return render(request, 'payment/pay.html', context={'error': 'Wrong Account Detail or amount'})

    transaction = Transaction.objects.create(user=user, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.user.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
    ) # CALLBACK_URl needs to change with domain 
    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'payment/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        paytm_checksum = ''
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            donePayment = "['TXN_SUCCESS']"
            print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
            return render(request, 'payment/callback.html', context=received_data)
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payment/callback.html', context=received_data)
        return render(request, 'payment/callback.html', context=received_data)
    else:
        context = {
            "error" : 1,
        }
        return render(request, 'payment/callback.html', context)

@login_required
def paymentCallback(request):
    # pass
    if request.method == "POST":
        user = request.user
        received_data = request.POST
        if received_data:
            if str(received_data['STATUS']) == "['TXN_SUCCESS']" and received_data['BANKTXNID']:
                print("---------- Updating payment status in account ---------------")
                # logic to update in account
                return redirect('payment:payment_info')
            elif str(received_data['STATUS']) == "['TXN_FAILURE']":
                print("------------- Payment Failed -----------------")
                return redirect('payment:pay')
        else:
            raise ValueError("Payment before enrollment!")
        return render(request, 'payment/paymentCallback.html', context=None)
    else:
        project_list = Service.objects.filter(service_id = request.user.service_user)
        print("-------------------->", project_list)
        context = {
            'projects': project_list
        }
        return render(request, 'payment/paymentCallback.html', context)
