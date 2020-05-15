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
        try:
            user_per = Group.objects.get(user=request.user)
        except:
            return HttpResponseRedirect('/')
        if str(user_per) == 'admin' or request.method == 'GET':
            return True
        else:
            return HttpResponseRedirect('/')

class LoginAuth(APIView):

    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')

class UserInfo(APIView):

    permission_classes = [MyPers]

    '''    def dispatch(self, request, *args, **kwargs):
        

        for g in group_list:
            print(g.get("name"))

        result = super(UserInfo,self).dispatch(request, *args, **kwargs)
        return result'''


    def get(self,request,*args,**kwargs):
        group_list = list(Group.objects.values())

        if request.GET.get('type') is not None:
            user_dict = {}
            user_data = []
            for l in list(User.objects.values()):
                a = User.objects.get(username=l.get('username'))
                user_dict['username'] = l.get('username')
                user_dict['email'] = l.get('email')
                user_dict['groups'] = a.groups.get().name
                user_data.append(user_dict)
                user_dict = {}
            return HttpResponse(str(dumps(user_data)))
        else:
            return render(request,'user_list.html',locals())

    def put(self,request,*args,**kwargs):
        data = eval(sub('\[|\]', '', str(dict(request.POST))))
        u = User.objects.get(username=data.get('username'),email=data.get('email'))
        g = Group.objects.get(name=data.get('groups'))
        u.groups.clear()
        u.groups.add(g.id)
        return HttpResponse(1)

    def post(self,request,*args,**kwargs):
        data = eval(sub('\[|\]', '', str(dict(request.POST))))
        u = User.objects.filter(username=data.get('username'))
        #判断提交的内容是否有误
        if '' in data.values():
            return HttpResponse(1)

        if u.count() == 0:
            User.objects.create_superuser(**data)
            Create_u = User.objects.get(username=data.get('username'))
            g_id = Group.objects.get(name='test')
            g_id.user_set.add(Create_u.id)
            return HttpResponse(0)

        return HttpResponse(u.count())

    def delete(self,request,*args,**kwargs):
        data = eval(sub('\[|\]', '', str(dict(request.POST))))
        u = User.objects.filter(username=data.get('username'),email=data.get('email'))
        u.delete()
        return HttpResponse(1)

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
