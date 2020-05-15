#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Content,Service_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from json import dumps

#默认页面及认证页面和跳转
def user_login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')

    return render(request,'login.html')

def index(request):
    '''
    登陆页面

    '''
    map = [
        {'name': "海门", 'value': 9},
        {'name': "鄂尔多斯", 'value': 12},
        {'name': "招远", 'value': 50},
        {'name': "舟山", 'value': 12},
        {'name': "齐齐哈尔", 'value': 14},

    ]
    service_num = Service_data.objects.all().count()

    return render(request, 'index.html', locals())

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def settings(request):
    '''
    设置页面
    '''
    err ={'err':'None'}
    if request.method == "POST":
        post_data = str(dict(request.POST))
        post_data = post_data.replace('[', '')
        post_data = eval(post_data.replace(']', ''))

        print(request.POST.get('image'))
        err = '成功：数据配置更新完成'
    return render(request,'settings.html',err)

def set_passwd(request):
    '''
    密码修改
    '''
    if request.method == 'GET':
        return render(request,'settings.html')

    if request.method == 'POST':

        if request.POST.get('set_passwd') != request.POST.get('ok_passwd') or request.POST.get('set_passwd') == '':

            err = '错误：两次输入的密码不一致，请重新输入'
            return  render(request,'settings.html',locals())
        u = User.objects.get(username=request.user)
        u.set_password(request.POST.get('set_passwd'))
        u.save()
        logout(request)
        return HttpResponseRedirect("/")


def task_temp(request):

    return render(request,'task_temp.html')

def user_html(request):
    '''
        用户列表
    '''
    if request.is_ajax():
        if request.GET.get('request_type') == 'get_data':
            total_list = []
            dic = {}
            for u in User.objects.all():
                dic['id'] = u.id
                dic['username'] = u.username
                dic['email'] = u.email
                dic['groups'] = [y['name'] for y in u.groups.values() ]

                total_list.append(dic)
                dic = {}

            service_data = dumps(total_list)

            return HttpResponse(str(service_data))

        elif request.POST.get('request_type') == 'remove_data':

            drop_data = User.objects.get(id=request.POST.get('id')).delete()
            return HttpResponse("ok")

        elif request.POST.get('request_type') == 'create_user':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            User.objects.create_superuser(username=username, password=password, email=email)
            return HttpResponse('ok')
        elif request.POST.get('request_type') == 'edit_data':

            post_data = str(dict(request.POST))
            post_data = post_data.replace('[', '')
            post_data = eval(post_data.replace(']', ''))
            g_update = 0

            if post_data['post_group'] != '':

                u = User.objects.get(username=post_data['username'])

                g_id = []
                for x in post_data['post_group'].split(','):

                    g_id.append(Group.objects.get(name=x).id)

                    u.groups.set(g_id)
                g_update = 2
            del post_data['post_group']
            del post_data['request_type']

            del  post_data['groups']
            if User.objects.filter(**post_data).count() < 1:
                edit_remark = User.objects.filter(username=post_data['username'])
                edit_remark.update(**post_data)

                return HttpResponse(1)
            return HttpResponse(g_update)

    return render(request,'user_list.html')

def info_temp(request):

    return render(request,'info_temp.html')


def txt_html(request):


    if request.is_ajax():
        if request.GET.get('request_type') == 'get_data':
            total_list = []
            dic = {}
            for f in Content.objects.all():
                dic['id'] = f.id
                dic['file_name'] = f.file_name
                dic['file_remark'] = f.file_remark
                dic['file_content'] = f.file_content
                total_list.append(dic)
                dic = {}

            service_data = dumps(total_list)

            return HttpResponse(str(service_data))
        elif request.method == 'POST' and request.POST.get('request_type') == 'remove_data':

            Content.objects.filter(id=request.POST.get('id')).delete()
            return HttpResponse('ok')
    elif request.path == '/file_create/':
        return  render(request,'file.html')
    return render(request,'txt_list.html')

def file_html(request,file_id):

    if request.user.is_authenticated:
        file_content = Content.objects.get(id=file_id).file_content
        file_name = Content.objects.get(id=file_id).file_name
        file_remark = Content.objects.get(id=file_id).file_remark
        if request.method == 'GET':

            return render(request,'file.html',locals())
        elif request.is_ajax():
            if request.method == 'POST' and request.POST.get('request_type') == 'file_modify':
                Content.objects.filter(
                    id = file_id).update(file_remark = request.POST.get('file_remark'),
                    file_name=request.POST.get('file_name'),
                                              file_content=request.POST.get('file_content'))
                return render(request, 'file.html', locals())


# Create your views here.
