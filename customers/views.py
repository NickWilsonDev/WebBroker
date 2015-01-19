from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from models import CustomerForm, Customer


# Create your views here.
@login_required
def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return render(request, 'loads/broker.html')
    else:
        form = CustomerForm()
    return render(request, 'customers/newCustomer.html', {'form': form})

@login_required
def listCustomers(request):
    customers = Customer.objects.order_by('company_name')
    return render(request, 'customers/customerList.html', {'customers': customers})

@login_required
def customerDetail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customerDetail.html', {'customer': customer})
    
