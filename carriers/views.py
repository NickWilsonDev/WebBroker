from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


from models import CarrierForm, Carrier


# Create your views here.

@login_required
def newCarrier(request):
    if request.method == "POST":
        form = CarrierForm(request.POST)
        if form.is_valid():
            carrier = form.save(commit=False)
            carrier.save()
            return render(request, 'loads/broker.html')
    else:
        form = CarrierForm()
    return render(request, 'carriers/newCarrier.html', {'form': form})

@login_required
def listCarriers(request):
    carriers = Carrier.objects.order_by('company_name')
    return render(request, 'carriers/carrierList.html', {'carriers': carriers})

@login_required
def carrierDetail(request, pk):
    carrier = get_object_or_404(Carrier, pk=pk)
    return render(request, 'carriers/carrierDetail.html', {'carrier': carrier})

@login_required
def carrierEdit(request, pk):
    carrier = get_object_or_404(Carrier, pk=pk)
    if request.method == "POST":
        form = CarrierForm(request.POST, instance=carrier)
        if form.is_valid():
            carrier = form.save(commit=False)
            carrier.save()
            return render(request, 'carriers/carrierDetail.html', {'carrier':carrier})
    else:
        form = CarrierForm(instance=carrier)
    return render(request, 'carriers/carrierEdit.html', {'form':form})

