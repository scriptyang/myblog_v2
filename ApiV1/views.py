from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from json import dumps
from assets.models import Service_data
from re import sub
from django.contrib.auth.models import Group,User
from rest_framework.permissions import BasePermission

class MyPers(BasePermission):
    def has_permission(self, request, view):
        user_per = Group.objects.get(user=request.user)
        if str(user_per) == 'admin' or request.method == 'GET':
            return True
        else:
            return False

class LoginAuth(APIView):

    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')

class UserInfo(APIView):

    permission_classes = [MyPers]

    def get(self,request,*args,**kwargs):

        if request.GET.get('type') is not None:

            user_data = list(User.objects.values())
            print(user_data)
            return HttpResponse(str(user_data))
        else:
            return render(request,'user_list.html',locals())


class ServiceInfo(APIView):


    permission_classes = [MyPers]

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
