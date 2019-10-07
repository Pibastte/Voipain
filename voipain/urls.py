from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'freckly'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('newUser', views.NewUser, name='newuser')
]
