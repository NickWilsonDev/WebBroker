from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# jsonify stuff###############
from django.core import serializers
#############################
from models import Load, LoadForm
from jobs.models import Job
from customers.models import Customer
from carriers.models import Carrier

import datetime

# Create your views here.

def index(request):
    """
        View simply renders the index.html document.
    """
    return render_to_response('loads/index.html')

def about(request):
    """
        View renders the about page.
    """
    return render_to_response('loads/about.html')

def missionStatement(request):
    """
        View renders the mission statement page.
    """
    return render_to_response('loads/missionStatement.html')

def customerContact(request):
    """
        View renders the customerContact page.
    """
    return render_to_response('loads/customerContact.html')

def carrierContact(request):
    """
        View renders the carrier contact page.
    """
    return render_to_response('loads/carrierContact.html')

###### view for user login #########
def user_login(request):
    """
        View renders the login page and provides the logic to authenticate the
        user.
    """
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                today = datetime.date.today()
                loads = getListLoads(today)
                customerList = getCustomerList()
                carrierList = getCarrierList()
                return render(request, 'loads/broker.html', {'loads': loads, 'customerList': customerList, 'carrierList': carrierList})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your AllPoints account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'loads/login.html', {})


def getListLoads(theday):
    """
        Function queries the Load table and returns a list of loads based on
        the date given as a parameter.
        @param
            theday - a date
        @return
            loads - a list of load objects
    """
    loads = Load.objects.filter(date=theday).order_by('pk')
    return loads

@login_required
def home(request):
    """
        Function gets the current date and then lists all loads that take
        place on the the current date. It then renders the basic listLoads.html
        template with the appropriate loads data.
    """
    today = datetime.date.today()
    loads = getListLoads(today)

    customerList = getCustomerList()
    carrierList = getCarrierList()
    loads = []

    return render(request, 'loads/listLoads.html', {'loads': loads, 'customerList':customerList, 'carrierList':carrierList})
    #return render(request, 'loads/listLoads.html', {'loads': loads})


def convertDateFormat(date):
    """
        Function converts date string to the correct format and returns it.
        @param
            date - a string representing the date
        @returns
            newdate - a string with the correct format of the date
    """
    newdate = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    return newdate

def getLoadsByOriginCity(city):
    """
        Function queries the database for all loads that begin in the city that
        is given in the parameter.
        @param
            city - String that represents the origin city for a load
        @returns
            loads - all loads that begin in the city given by the parameter
    """ 
    loads = Load.objects.filter(origin_city__iexact=city).order_by('pk')
    return loads

def getLoadsByOriginState(state):
    loads = Load.objects.filter(origin_state__iexact=state).order_by('pk')
    return loads

def getLoadsByDestinationState(state):
    loads = Load.objects.filter(reciever_state__iexact=state).order_by('pk')
    return loads

def getLoadsByCarrier(carrierName):
    loads = Load.objects.filter(carrier__iexact=carrierName).order_by('pk')
    return loads

def getLoadsByCustomer(customerName):
    loads = Load.objects.filter(customer__iexact=customerName).order_by('pk')
    return loads


def getCustomerList():
    """
        Function returns a list of tuples that contain the customer's companies
        names.
        @return
            customerList - list of tuples of the customer's company names.
    """
    customerList = Customer.objects.order_by('company_name')
    custList = []
    for customer in customerList:
        tempTuple = [(customer.company_name), (customer.company_name)]
        custList.append(tempTuple)
    customerList = []
    customerList = [x[0].encode('utf-8') for x in custList]
    return customerList

def getCarrierList():
    """
        Function returns a list of tuples that contain the carrier's companies
        names.
        @return
            carrierList - list of tuples of the carrier's company names.
    """
    carrierList = Carrier.objects.order_by('company_name')
    carrList = []
    for carrier in carrierList:
        tempTuple = [(carrier.company_name), (carrier.company_name)]
        carrList.append(tempTuple)
    carrierList = []
    carrierList = [x[0].encode('utf-8') for x in carrList]
    return carrierList


@login_required
def listLoads(request):
    """
        These are the basic 'search' functions for use by the user.
    """
    customerList = getCustomerList()
    carrierList = getCarrierList()
    loads = []

    if 'targetDate' in request.POST:
        targetDate = request.POST['targetDate']
        newdate = convertDateFormat(targetDate)
        loads = getListLoads(newdate)
    elif 'originCity' in request.POST:
        city = request.POST['originCity']
        loads = getLoadsByOriginCity(city)
    elif 'originState' in request.POST:
        state = request.POST['originState']
        loads = getLoadsByOriginState(state)
    elif 'destState' in request.POST:
        state = request.POST['destState']
        loads = getLoadsByDestinationState(state)
    elif 'customerName' in request.POST:
        customerName = request.POST['customerName']
        loads = getLoadsByCustomer(customerName)
    elif 'carrierName' in request.POST:
        carrierName = request.POST['carrierName']
        loads = getLoadsByCarrier(carrierName)
    return render(request, 'loads/listLoads.html', {'loads': loads, 'customerList':customerList, 'carrierList':carrierList})

@login_required
def loadDetail(request, pk):
    load = get_object_or_404(Load, pk=pk)
    return render(request, 'loads/loadDetail.html', {'load': load})

@login_required
def loadConfirm(request, pk):
    load = get_object_or_404(Load, pk=pk)
    return render(request, 'loads/loadConfirmation.html', {'load':load})

########## user logout #############
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def newLoad(request):

    jobs = Job.objects.order_by('job_name') #all()
    print jobs
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++"
####### serialize jobs queryset to json object and then pass that to template
    jobs = serializers.serialize('json', jobs)
    print jobs

    if request.method == "POST":
        form = LoadForm(request.POST)
        if form.is_valid():
            load = form.save(commit=False)
            loadCarrier = Carrier.objects.get(company_name = load.carrier)
            load.carrierFax = loadCarrier.fax_number
            load.carrierEmail = loadCarrier.email
            load.save()
            today = datetime.date.today()
            loads = getListLoads(today)
            return render(request, 'loads/broker.html', {'loads':loads})
        else:
            print form.errors
    else:
        form = LoadForm()

    return render(request, 'loads/newLoad.html', {'form': form, 'jobs': jobs})

@login_required
def loadEdit(request, pk):
    load = get_object_or_404(Load, pk=pk)
    if request.method == "POST":
        form = LoadForm(request.POST, instance=load)
        if form.is_valid():
            load = form.save(commit=False)
            load.save()
            return render(request, 'loads/loadDetail.html', {'load':load})
    else:
        form = LoadForm(instance=load) 
    return render(request, 'loads/loadEdit.html', {'form': form})


@login_required
def loadDelete(request, pk):
    load = get_object_or_404(Load, pk=pk)
    loads = getListLoads(load.date)
    load.delete()
    return render(request, 'loads/listLoads.html', {'loads': loads})
