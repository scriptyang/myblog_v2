from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic.base import View
from rest_framework import mixins,generics
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from json import dumps
from assets.models import Service_data
from re import sub

class LoginAuth(APIView):


    def post(self,request,*args,**kwargs):

        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')

class ServiceInfo(APIView):

    def get(self,request,*args,**kwargs):
        if request.GET.get('type') is not None:
            service_data = dumps(list(Service_data.objects.values()))
            return HttpResponse(str(service_data))
        else:
            return render(request,'service_info.html')

    def put(self,request,*args,**kwargs):

        data = eval(sub('\[|\]', '',str(dict(request.POST))))
        res = Service_data.objects.filter(name=data['name']).update(**data)

        return HttpResponse(res)

    def delete(self, request, *args, **kwargs):
        drop_data = Service_data.objects.get(name=request.POST.get('id')).delete()
        return HttpResponse("ok")


# Create your views here.
