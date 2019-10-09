#coding: utf-8

from django.urls import path
from .views import *

urlpatterns = [
    path('LoginAuth/',LoginAuth.as_view(),name='login'),
    path('Service_info/',ServiceInfo.as_view(),name='service_info')
]