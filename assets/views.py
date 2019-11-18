#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Settings_cmdb,Content,Service_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from json import dumps

def ajax_request(request,models_name):
    if request.GET.get('request_type') == 'get_data':

        service_data = dumps(list(models_name.objects.values()))

        return HttpResponse(str(service_data))

    elif request.POST.get('request_type') == 'post_data':
        data = '''
            1809D55661,winc00036,172.2.2.4,172.1.0.36
    1809D55666,winc00034,172.2.0.18,172.1.0.34
    1808C5405,winc00003,172.2.2.2,172.1.0.3
    1805D3063,winc00042,172.2.0.4,172.1.0.42
    1808C5404,winc00043,172.2.0.20,172.1.0.43
    1808C5403,winc00044,172.2.0.22,172.1.0.44
    1808C5406,winc00045,172.2.0.24,172.1.0.45
    278110031,winc00046,172.2.0.26,172.1.0.46
    278110018,winc00047,172.2.0.28,172.1.0.47
    278110030,winc00048,172.2.0.30,172.1.0.48
    278110024,winc00049,172.2.0.32,172.1.0.49
    278110013,winc00050,172.2.0.34,172.1.0.50
    278110042,winc00051,172.2.0.36,172.1.0.51
    278110004,winc00052,172.2.0.38,172.1.0.52
    288550030,winc00053,172.2.0.40,172.1.0.53
    278110002,winc00054,172.2.0.42,172.1.0.54
    278110015,winc00055,172.2.0.44,172.1.0.55
    278110001,winc00056,172.2.0.46,172.1.0.56
    278110044,winc00057,172.2.0.48,172.1.0.57
    278110014,winc00058,172.2.0.50,172.1.0.58
    278110043,winc00059,172.2.0.52,172.1.0.59
    278110010,winc00060,172.2.0.54,172.1.0.60
    278110046,winc00061,172.2.0.56,172.1.0.61
    278110036,winc00062,172.2.0.58,172.1.0.62
    278110048,winc00063,172.2.0.60,172.1.0.63
    278110019,winc00064,172.2.0.62,172.1.0.64
    278110023,winc00065,172.2.0.64,172.1.0.65
    278110050,winc00066,172.2.0.66,172.1.0.66
    288550009,winc00067,172.2.0.68,172.1.0.67
    278110009,winc00068,172.2.0.70,172.1.0.68
    278110034,winc00069,172.2.0.72,172.1.0.69
    288550012,winc00070,172.2.0.74,172.1.0.70
    278110033,winc00071,172.2.0.76,172.1.0.71
    278110032,winc00072,172.2.0.78,172.1.0.72
    278110028,winc00073,172.2.0.80,172.1.0.73
    288550029,winc00074,172.2.0.82,172.1.0.74
    278110026,winc00075,172.2.0.84,172.1.0.75
    288550032,winc00076,172.2.0.86,172.1.0.76
    288550011,winc00077,172.2.0.88,172.1.0.77
    278110017,winc00078,172.2.0.90,172.1.0.78
    288550031,winc00079,172.2.0.92,172.1.0.79
    278110035,winc00080,172.2.0.94,172.1.0.80
    278110099,winc00081,172.2.0.96,172.1.0.81
    278110025,winc00082,172.2.0.98,172.1.0.82
    278110016,winc00083,172.2.0.100,172.1.0.83
    278110047,winc00084,172.2.0.102,172.1.0.84
    1808B5133,winc00085,172.2.0.104,172.1.0.85
    1806D3857,winc00086,172.2.0.106,172.1.0.86
    1808C5410,winc00087,172.2.0.108,172.1.0.87
    1808C5409,winc00088,172.2.0.110,172.1.0.88
    1808C5408,winc00089,172.2.0.112,172.1.0.89
    1808C5407,winc00090,172.2.0.114,172.1.0.90
    288550010,winc00091,172.2.0.116,172.1.0.91
    278110029,winc00092,172.2.0.118,172.1.0.92
    278110097,winc00093,172.2.0.120,172.1.0.93
    278110003,winc00094,172.2.0.122,172.1.0.94
    278110012,winc00095,172.2.0.124,172.1.0.95
    278110027,winc00096,172.2.0.126,172.1.0.96
    278110020,winc00097,172.2.0.128,172.1.0.97
    278110041,winc00098,172.2.0.130,172.1.0.98
    278110022,winc00099,172.2.0.132,172.1.0.99
    278110011,winc00100,172.2.0.134,172.1.0.100
    1809D55663,winc00101,172.2.0.136,172.1.0.101
    1809D55677,winc00102,172.2.0.138,172.1.0.102
    1809D55669,winc00103,172.2.0.140,172.1.0.103
    288550059,winc00104,172.2.0.142,172.1.0.104
    288550061,winc00105,172.2.0.144,172.1.0.105
    288550062,winc00106,172.2.0.146,172.1.0.106
    288550077,winc00107,172.2.0.148,172.1.0.107
    deamon,winc00160,172.2.0.254,172.1.0.160
    deamon,winc00161,172.2.1.2,172.1.0.161
    1809D55674,winc00028,172.2.2.14,172.1.0.28
    1808B5132,winc00023,172.2.2.12,172.1.0.23
    1809D55671,winc00031,172.2.0.14,172.1.0.31
    1809D55675,winc00025,172.2.2.6,172.1.0.25
    1809D55676,winc00026,172.2.2.20,172.1.0.26
    1809D55660,winc00037,172.2.2.22,172.1.0.37
    1809D55664,winc00040,172.2.2.24,172.1.0.40
    1809D55662,winc00039,172.2.2.26,172.1.0.39
    1809D55659,winc00035,172.2.2.28,172.1.0.35
    1808B5131,winc00018,172.2.2.36,172.1.0.18
    1808C5402,winc00013,172.2.2.42,172.1.0.13
    1809D55670,winc00015,172.2.2.40,172.1.0.15
    1806D3856,winc00009,172.2.2.38,172.1.0.9
    1809D55665,winc00022,172.2.2.44,172.1.0.22
    1805D3061,winc00002,172.2.2.48,172.1.0.2
    1809D55678,winc00029,172.2.2.76,172.1.0.29
    1805D3062,winc00004,172.2.2.52,172.1.0.4
    1806D3860,winc00005,172.2.2.54,172.1.0.5
    1806D3859,winc00006,172.2.2.56,172.1.0.6
    1806D3858,winc00008,172.2.2.58,172.1.0.8
    1808C5401,winc00012,172.2.2.62,172.1.0.12
    1808B5129,winc00019,172.2.2.64,172.1.0.19
    1809D55672,winc00032,172.2.2.68,172.1.0.32
    1809D55673,winc00033,172.2.2.70,172.1.0.33'''

        for d in data.split('\n'):
            if d != '' :
                sn, n, ov, pv = d.split(',')
                Service_data.objects.get_or_create(name=n, sn_num=sn, ssl=ov, ppp=pv)
        return HttpResponse('ok')
    elif request.POST.get('request_type') == 'remove_data':
        drop_data = models_name.objects.get(name=request.POST.get('id')).delete()
        return HttpResponse("ok")

    elif request.POST.get('request_type') == 'edit_data':

        post_data = str(dict(request.POST))
        post_data = post_data.replace('[', '')
        post_data = eval(post_data.replace(']', ''))
        del post_data['request_type']

        if models_name.objects.filter(**post_data).count() < 1:
            edit_remark = models_name.objects.filter(name=post_data['name'])
            edit_remark.update(**post_data)

            return HttpResponse(1)
        return HttpResponse(0)

# 返回html 文件 模板 函数
def request_html(request,html_name,err='None'):


    map = [
                {'name': "海门", 'value': 9},
                {'name': "鄂尔多斯", 'value': 12},
                {'name': "招远", 'value': 50},
                {'name': "舟山", 'value': 12},
                {'name': "齐齐哈尔", 'value': 14},

            ]
    err =  err
    group_list = [y for y in Group.objects.values()]
    set_var = Settings_cmdb.objects.values()[0]

    return render(request, html_name + '.html', locals())


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

def service_html(request):
    '''
    服务信息表格获取信息、删除、编辑
    '''


    return request_html(request, 'service_info')

def settings(request):
    '''
    设置页面
    '''
    err ='None'
    if request.method == "POST":
        post_data = str(dict(request.POST))
        post_data = post_data.replace('[', '')
        post_data = eval(post_data.replace(']', ''))
        Settings_cmdb.objects.update(**post_data)
        print(request.POST.get('image'))
        err = '成功：数据配置更新完成'
    return request_html(request,'settings',err)

def set_passwd(request):
    '''
    密码修改
    '''
    if request.method == 'GET':
        return request_html(request,'settings')

    if request.method == 'POST':

        if request.POST.get('set_passwd') != request.POST.get('ok_passwd') or request.POST.get('set_passwd') == '':

            pass_err = '错误：两次输入的密码不一致，请重新输入'
            return  request_html(request,'settings',pass_err)
        u = User.objects.get(username=request.user)
        u.set_password(request.POST.get('set_passwd'))
        u.save()
        logout(request)
        return HttpResponseRedirect("/")


def task_temp(request):

    return request_html(request,'task_temp')

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

    return request_html(request,'user_list')

def info_temp(request):

    return request_html(request,'info_temp')


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
        return  request_html(request,'file')
    return request_html(request,'txt_list')

def file_html(request,file_id):
    set_var = Settings_cmdb.objects.values()[0]
    var = conf
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
