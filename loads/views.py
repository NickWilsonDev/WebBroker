from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from models import Load, LoadForm
import datetime

# Create your views here.
def index(request):
    return render_to_response('loads/index.html')

def about(request):
    return render_to_response('loads/about.html')

def missionStatement(request):
    return render_to_response('loads/missionStatement.html')

def customerContact(request):
    return render_to_response('loads/customerContact.html')

def carrierContact(request):
    return render_to_response('loads/carrierContact.html')

###### view for user login #########
def user_login(request):

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
                return render(request, 'loads/broker.html', {'loads': loads})
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
    loads = Load.objects.filter(date=theday).order_by('pk')
    return loads

@login_required
def home(request):
    today = datetime.date.today()
    loads = getListLoads(today)
    return render(request, 'loads/listLoads.html', {'loads': loads})

def convertDateFormat(date):
    newdate = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    return newdate

def getLoadsByOriginCity(city):
    loads = Load.objects.filter(origin_city=city).order_by('pk')
    return loads

def getLoadsByOriginState(state):
    loads = Load.objects.filter(origin_state=state).order_by('pk')
    return loads

def getLoadsByDestinationState(state):
    loads = Load.objects.filter(reciever_state=state).order_by('pk')
    return loads

@login_required
def listLoads(request):
    """
        These are the basic 'search' functions for use by the user.
    """
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

    return render(request, 'loads/listLoads.html', {'loads': loads})

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
    if request.method == "POST":
        form = LoadForm(request.POST)
        if form.is_valid():
            load = form.save(commit=False)
            load.save()
            today = datetime.date.today()
            loads = getListLoads(today)
            return render(request, 'loads/broker.html', {'loads':loads})
        else:
            print form.errors
    else:
        form = LoadForm()
    return render(request, 'loads/newLoad.html', {'form': form})

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
        form = LoadForm(instance=load) #instance=post before in ()
    return render(request, 'loads/loadEdit.html', {'form': form})


@login_required
def loadDelete(request, pk):
    load = get_object_or_404(Load, pk=pk)
    loads = getListLoads(load.date)#targetDate)
    load.delete()
    return render(request, 'loads/listLoads.html', {'loads': loads})
