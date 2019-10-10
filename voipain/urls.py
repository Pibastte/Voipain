from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'freckly'
urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('demandes', views.SeeDemands.as_view(), name='seedemands'),
    path('demander', views.RegisterDemand.as_view(), name='registerdemand'),
    path('newDemand', views.NewDemand, name='newdemand'),
    path('newPickUp', views.NewPickUp, name='newpickup'),
    path('checkPickUp', views.CheckPickUp.as_view(), name='checkpickup')
]
