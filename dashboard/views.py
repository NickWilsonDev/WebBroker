import sys 

import json
from django.db.models import Count

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime


from loads.models import Load

# Create your views here.


@login_required
def getData(request):
    loads = Load.objects.order_by('commodity')

    return JsonResonse(loads, safe=False)

@login_required
def dashboardBase(request):
    loadsByCommodity = Load.objects.values('commodity').order_by().annotate(Count('commodity'))
    loadsByCarrier = Load.objects.values('carrier').order_by().annotate(Count('carrier'))
    loadsByCustomer = Load.objects.values('customer').order_by().annotate(Count('customer'))

    loadsOverTime = Load.objects.values('commodity', 'date').order_by('date')
    
    print sys.getsizeof(loadsOverTime)
    print loadsOverTime
    return render(request, 'dashboard/dashboard.html', {'loadsByCommodity': loadsByCommodity, 'loadsByCarrier': loadsByCarrier, 'loadsByCustomer': loadsByCustomer, 'loadsOverTime': loadsOverTime})
