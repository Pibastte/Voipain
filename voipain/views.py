from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader

from pathlib import Path

from voipain.models import User

import datetime

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'voipain/index.html'

    def get_queryset(self):
        return True

def NewUser(request):
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
