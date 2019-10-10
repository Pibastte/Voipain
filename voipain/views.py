from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader

from pathlib import Path

from voipain.models import User

import datetime

# Create your views here.

class RegisterDemand(generic.ListView):
    template_name = 'voipain/registerDemand.html'

    def get_queryset(self):
        return True

class IndexView(generic.ListView):
    template_name = 'voipain/index.html'

    def get_queryset(self):
        return True

class SeeDemands(generic.ListView):
    template_name = 'voipain/seeDemands.html'
    context_object_name = 'demands'

    def get_queryset(self):
        return User.objects.filter(date=datetime.date.today()).filter(pickedUp=False)

class CheckPickUp(generic.ListView):
    template_name = 'voipain/seeDemandsPickedUp.html'
    context_object_name = 'demands'

    def get_queryset(self):
        return User.objects.filter(date=datetime.date.today()).filter(pickedUp=True)

# POST
def NewDemand(request):
    print(request.POST)
    print(request.POST['name'])
    print(request.POST['adress'])
    print(request.POST['numberBaguette'])

    if (User.objects.filter(name=request.POST['name']).count() == 0):
        u = User(name=request.POST['name'], date=datetime.date.today(), adress=request.POST['adress'], number=request.POST['numberBaguette'])
    else:
        u = User.objects.get(name=request.POST['name'])
        u.date = datetime.date.today()
    u.save()

    return HttpResponseRedirect('/')

def NewPickUp(request):
    print(request.POST['adress'])
    if (User.objects.filter(name=request.POST['name']).count() != 0):
        u = User.objects.get(name=request.POST['name'])
        u.adressPickUp = request.POST['adress']
        u.pickedUp = True
        u.save()
    return HttpResponseRedirect('/')
