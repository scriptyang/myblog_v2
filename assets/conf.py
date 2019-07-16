#conding: utf-8
from .models import Service_data

conf = {
    "table_url": {
        "service_info":"服务信息",
    },
    "user_url": {
        'user_list': "用户列表"
    },
    "txt_url": {
        'txt_list': "文 档"
    },
    "temp_url": {
        'task_temp': "任务工单",
        "info_temp": "信 息"
    },
    #name 和 remark 不需要进行匹配
    "data_structure":{
        "name": "vpn账号",
        "sn_num": "sn号码",
        "ssl": "sslip",
        "ppp": 'xl2ip',
        "remark": "备注"
    },
    "user_structure":{
        "id": "id",
        "username": "用户",
        "email": "邮箱",
        "groups": '用户组',
    },
    "service_num": Service_data.objects.all().count(),
}

