from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from ecorpin.models import Ecorpian

# Create your views here.
def index_bbit(request):
    #Content Query
    dev = Ecorpian.objects.get(name='Bhagwan Singh')
    print("------->", dev)
    context = {
        'devName': str(dev),
    }
    return render(request, 'bbit/index.html', context)
